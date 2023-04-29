import re
import keyboard_layout


def get_key_name(key):
    if key == '\t':
        return 'TAB'
    return str(key)

class Binding:

    def __init__(self, tag, repeats, actions, layout: keyboard_layout.KeyboardLayout):
        self.tag = tag
        self.repeats = repeats # TODO repeats validation?
        self.keytags = []  # [(type, [modifier], key)]
        self.action = None
        self.layout = layout

        for a in actions:
            if a.tag == self.tag:
                self.action = a
                a.register_binding(self)
                break

        self.convert = self.action.convert if self.action else False

    def __eq__(self, other):
        if self.tag != other.tag:
            return False
        if self.repeats != other.repeats:
            return False
        return self.keytags == other.keytags

    def get_ui(self, long=False):
        out = []
        for k in self.keytags:
            text = ""
            if k[0] == 'KEY':
                text = get_key_name(k[1])
            else:
                modifiers = [
                    # (0x01, 'Shift', "⇧"),
                    (0x02, 'Ctrl', "^"),
                    (0x01, 'Shift', "↑"),
                    # (0x04, 'Alt', "⌥"),
                    (0x04, 'Alt', "ª"),
                ]
                for byte, name, symbol in modifiers:
                    if int(k[1]) & byte:
                        if long:
                            text += name + ' '
                        else:
                            text += symbol
                if k[0] == "BUTTON":
                    if long:
                        text += "Mouse "
                    else:
                        text += 'M'
                text += get_key_name(k[2])

            out.append(text)
        return out

    def add_keytag(self, tag):
        t = None
        keymatch = re.match("\[KEY:(.*)]", tag)
        if keymatch:
            key = keymatch.group(1)
            if self.convert:
                key = self.layout.convert_from_qwerty(key)
            t = ('KEY', key)
        else:
            symmatch = re.match("\[SYM:([0-9]*):(.*)]", tag)
            if symmatch:
                key = symmatch.group(2)
                if self.convert:
                    key = self.layout.convert_from_qwerty(key)
                t = ('SYM', int(symmatch.group(1)), key)
            else:
                buttommatch = re.match("\[BUTTON:([0-9]*):([0-9]*)]", tag)
                if buttommatch:
                    t = ('BUTTON', int(buttommatch.group(1)), int(buttommatch.group(2)))
                else:
                    print("Ignoring unrecognized tag: {0}".format(tag))
        if t is not None:
            self.keytags.append(t)

    def express(self):
        out = ["[BIND:{0}:{1}]".format(self.tag, self.repeats)]
        for tag in self.keytags:
            out.append("[{0}]".format(
                ":".join([str(i) for i in tag])
            ))
        return "\n".join(out)


class Bindings:

    def __init__(self, interface_path: str, actions: list, layout: keyboard_layout.KeyboardLayout):

        self.bindings = []
        self.actions = actions
        self.layout = layout

        with open(interface_path, "r", encoding="cp437") as file:
            binding = None
            for line in file:
                bindmatch = re.match("\[BIND:(.*):(.*)]", line)
                if bindmatch:
                    binding = Binding(bindmatch.group(1), bindmatch.group(2), actions, layout)
                    self.bindings.append(binding)
                elif binding:
                    binding.add_keytag(line)

    def express(self):
        return "\n" + "\n".join([
            b.express() for b in self.bindings
        ])

    def difference(self, other_bindings):
        out = []
        for b in self.bindings:
            b_o = [i for i in other_bindings.bindings if i.tag == b.tag][0]

            if b != b_o:
                out.append((b, b_o))
        return out