import os
import shutil

from PIL.Image import Resampling

import action
import bindings
import changelog
import constants
import sprite_sheet

from PIL import Image, ImageDraw, ImageFont


class Mod:

    def __init__(self, name, id, keyboard_layout, hotkey_path, steam_id=None,
                 show_hotkeys=True, tagline=None, color=(102, 132, 163), description=None, image_path=None):
        self.name = name
        self.id = id
        self.keyboard_layout = keyboard_layout
        self.hotkey_path = hotkey_path
        self.steam_id = steam_id
        self.bind = bindings.Bindings(self.hotkey_path, action.get_actions(), self.keyboard_layout)
        self.show_hotkeys = show_hotkeys
        self.tagline = tagline if tagline else self.keyboard_layout.name
        self.color = color
        self.description = description if description else \
            "The HUD hints for a set of {0} friendly hotkeys and some " \
            "interface tweaks. "\
            "The hotkeys themselves must be installed by manually copying '{1}' to '{2}'.".format(
                self.keyboard_layout.name,
                'Dwarf Fortress/mods/{0}/interface.txt'.format(self.get_install_folder_id()),
                'Dwarf Fortress/prefs/interface.txt',
            )

        self.changes_hotkeys = self.hotkey_path != 'ref/interface_default.txt'
        self.image_path = image_path


    def get_steam_tags(self):
        return constants.STEAM_TAGS

    def get_version_number(self):
        return constants.get_version_number(constants.VERSION)

    def get_version_string(self):
        return constants.get_version_string(constants.VERSION)

    def get_install_folder_id(self):
        return "{0} ({1})".format(self.steam_id, self.get_version_number())

    def generate_info_txt(self):
        lines = [
            "[ID:{0}]".format(self.id),
            "[NUMERIC_VERSION:{0}]".format(self.get_version_number()),
            "[DISPLAYED_VERSION:{0}]".format(constants.get_version_string(constants.VERSION)),
            "[EARLIEST_COMPATIBLE_NUMERIC_VERSION:{0}]".format(constants.get_version_number(
                constants.get_earliest_compatible_version())),
            "[EARLIEST_COMPATIBLE_DISPLAYED_VERSION:{0}]".format(constants.get_version_string(
                constants.get_earliest_compatible_version())),
            "[AUTHOR:Trainzack]",
            "[NAME:{0}]".format(self.name),
            "[DESCRIPTION:{0}]".format(
                self.description
            ),
            "",
            "[STEAM_FILE_ID:{0}]".format(
                self.steam_id) if self.steam_id is not None else "No steam ID!",
            "[STEAM_TITLE:{0}]".format(self.name),
        ] + ["[STEAM_TAG:{0}]".format(t) for t in self.get_steam_tags()] + [
        ] + ["[STEAM_METADATA:{0}]".format(t) for t in constants.STEAM_METADATA] + [
            "[STEAM_CHANGELOG:Version {0} {1}]".format(
                constants.VERSION_STRING,
                " -=- ".join(changelog.get_most_recent_changes()).replace(":", ";").replace("]", "|")
            )
        ]
        if self.id != 'interface_tweaks':
            lines.append("\n[CONFLICTS_WITH_ID:interface_tweaks]")
        return "\n".join(lines)

    def shadow_text(self, drawer, location, text, font, distance=2):

        drawer.text(
            xy=(location[0] + distance, location[1] + distance),
            text=text,
            font=font,
            fill=(0, 0, 0, 255),
            anchor='mm',
        )
        drawer.text(
            xy=location,
            text=text,
            font=font,
            fill=(255, 255, 255, 255),
            anchor='mm',

        )

    def generate_description(self):
        out = [
            "[h1]{0} Version {1}[/h1]".format(self.name, self.get_version_string()),
        ]
        if self.changes_hotkeys:
            out.extend(self.generate_description_changes_hotkeys())
        else:
            out.extend(self.generate_description_default_hotkeys())
        return out

    def generate_description_default_hotkeys(self):
        out = []
        if self.show_hotkeys:
            out.extend([
                "This mod adds visible hotkeys to most actions that have hotkeys, replaces the disband squad button "
                "with a trash can so you stop disbanding squads on accident, makes the difference between selected "
                "and deselected UI icons more obvious, and many other minor improvements that should make "
                "the UI easier to use and understand."
            ])
        else:
            out.extend([
                "This mod includes many tweaks to the game's UI, including replacing the disband squad button with a "
                "trash can so you stop disbanding squads on accident, making the difference between selected and "
                "deselected UI icons more obvious, and many other minor improvements that should make "
                "the UI easier to use and understand."
            ])
        out.extend(self.section_other_versions())
        out.extend(self.section_issues())
        out.extend(self.section_liscence())
        return out

    def generate_description_changes_hotkeys(self):
        out = []
        out.extend([
            "This mod replaces the game's default hotkeys with a set of hotkeys designed to be easily accessed with the"
            " left hand alone. "
            "The hotkeys also closely mirror the layout of the buttons on screen for easy memorization. "
            "You can finally stop hunting all around your keyboard for the correct shortcut and rest your hand in a "
            "comfortable position! ",
            "",
        ])
        if self.keyboard_layout.name == 'QWERTY':
            out.append(
                "Because the quality of the keybindings are so heavily depends on your keyboard layout, there are "
                "multiple versions of this mod. "
                "If you aren't sure which version of this mod to get, then [b]this[/b] is probably the correct "
                "one (look at the top left of your keyboard to be sure)."
            )
        else:
            out.append(
                "Because the quality of the keybindings are so heavily depends on your keyboard layout, there are "
                "multiple versions of this mod. "
                "If you aren't sure which version of this mod to get, then the QWERTY version (not this one) "
                "is probably the correct one (look at the top left of your keyboard to be sure)."
            )
        out.extend([
            "",
            "This mod contains all of the improvements of my other mod, [b]Interface Tweaks[/b], including a better "
            "squad disband button, a colored pause button, and on-screen hotkeys for all buttons with shortcuts. "
        ])
        out.extend(self.section_other_versions())
        out.extend([
            '[h1]Installation[/h1]',
            "To install the hotkeys, you must manually copy '{0}' to '{1}'. You may want to make a backup "
            "first. ".format(
                        'Dwarf Fortress/mods/{0}/interface.txt'.format(self.get_install_folder_id()),
                        'Dwarf Fortress/prefs/interface.txt',
            ),
            "",
            "If you also want the interface tweaks and on-screen keyboard hints, you must install this mod into your "
            "world. "
            "You can do that either by selecting this mod when creating a new world, or if you already have "
            "[b]Interface Tweaks[/b] installed, by replacing the png files in that mod (in the "
            "installed_mods/interface_tweaks folder) with the png files in this one. "
            "You should make a backup first, as this type of installation is not officially supported by the game.",
        ])

        out.extend(self.section_changed())
        out.extend(self.section_issues())
        out.extend(self.section_liscence())

        return out

    def section_other_versions(self):

        text = "This mod is part of a collection of mods that each include the same UI tweaks, but with some " \
               "differences. " \
               "These include "

        if self.show_hotkeys:
            text += "versions that don't include hotkey hints, "
        else:
            text += "versions that have visible hotkey hints wherever possible, "
        if self.changes_hotkeys:
            text += "and versions that work with the default set of hotkeys"
        else:
            text += "and versions that have a custom set of easier to use hotkeys compatible with many keyboard layouts"
        text += "."

        out = [
            "[h1]Other Versions of this Mod[/h1]",
            text,
            "[url=https://steamcommunity.com/sharedfiles/filedetails/?id=2901379585]Browse the whole collection "
            "to find the mod that best suits your needs![/url]"
        ]

        return out

    def section_changed(self):
        out = [
            "[h1]Changed Hotkeys[/h1]",
            "Some hotkeys that I've changed cannot have UI hints, so here is a list of those:"
            "[table][tr][th]Action[/th][th]New Shortcut[/th][/tr]",
        ]
        for b in self.bind.bindings:
            if b.action is None or b.action.location is not None:
                continue
            out.append("[tr][td]{0}[/td][td]{1}[/td][/tr]".format(
                b.action.ui_name,
                ' or '.join(b.get_ui(True)),
            ))
        out.extend([
            "[/table]",
        ])
        return out

    def section_issues(self):
        issues = []
        if self.show_hotkeys:
            issues.extend([
                "[*]If you change any hotkeys, [b]the displayed hotkeys will be inaccurate[/b]. "
                "You are free to alter the mod to make it work with your hotkeys, if you have the patience. ",
                "[*]The hotkeys for the screw press and soapmaker's workshop are unchanged, and the hotkey hints are not "
                "shown. "
                "This is a bug in the base game that I cannot fix. ",
                "[*]There is no way to put different graphics on the buttons for the magma and non-magma furnaces, so both "
                "keys are listed.",
                "[*]The hotkeys are also listed when you select a placed building, though you can think of this as a "
                "feature if you'd like.",
            ])

        if self.changes_hotkeys:
            issues.extend([
                "[*]Not all keyboard layouts have been thoroughly tested. Please report any issues to me!",
            ])

        if len(issues) == 0:
            issues.append("[*]None known for this version of the mod.")


        out = [
            "[h1]Known Issues[/h1]",
            "[list]",
        ]
        out.extend(issues)
        out.extend([
            "[/list]",
        ])
        return out

    def section_liscence(self):
        return [
            "[h1]License[/h1]",
            "This mod is licensed under a Creative Commons Attribution-ShareAlike 4.0 International license. "
            "This means that you can use the contents of this work (as-is or modified) in your own work, even if "
            "you benefit financially, so long as you give proper attribution and license the work under the same "
            "license. "
            "You don't need to ask me first (though I would appreciate a heads up!).",
            "The license terms are [url=https://creativecommons.org/licenses/by-sa/4.0/]explained here[/url] and "
            "are [url=https://creativecommons.org/licenses/by-sa/4.0/legalcode]listed in full here[/url]."
        ]

    def generate_preview(self, folder):
        if self.image_path:
            with Image.open(self.image_path) as source:
                source.save(folder + 'preview.png')
        else:
            RESIZE = 3
            IMAGE_SIZE = 5 * (RESIZE * 32)
            preview = Image.new(mode='RGBA', size=(IMAGE_SIZE, IMAGE_SIZE), color=self.color)
            if os.path.exists('C:/Windows/Fonts/dejavuserifcondensed-bold.ttf'):
                font_path = 'C:/Windows/Fonts/dejavuserifcondensed-bold.ttf'
            else:
                font_path = 'ref/curses8x12.ttf'
            title_font = ImageFont.truetype(font_path, 78)
            sub_font = ImageFont.truetype(font_path, 36)
            draw = ImageDraw.Draw(preview)

            title_words = self.name.split(' ')
            offset = 55
            self.shadow_text(draw, (IMAGE_SIZE / 2, IMAGE_SIZE / 2 - 1.5 * offset), title_words[0], title_font, 4)
            self.shadow_text(draw, (IMAGE_SIZE / 2, IMAGE_SIZE / 2 + 0.5 * offset), title_words[1], title_font, 4)
            self.shadow_text(draw, (IMAGE_SIZE / 2, IMAGE_SIZE / 2 + 1.8 * offset), self.tagline, sub_font, 2)


            with Image.open(folder + 'graphics/images/interface_bits_tweaked.png') as source:
                for s_x, s_y, d_x, d_y in [
                    (256, 264, 0, 0),
                    (288, 264, 1 * (32 * RESIZE), 0),
                    (320, 264, 2 * (32 * RESIZE), 0),
                    (256, 300, 3 * (32 * RESIZE), 0),
                    (192, 228, 4 * (32 * RESIZE), 0),

                    (0, 264, 0, IMAGE_SIZE - (36 * RESIZE)),
                    (0, 624, 1 * (32 * RESIZE), IMAGE_SIZE - (36 * RESIZE)),
                    (64, 624, 2 * (32 * RESIZE), IMAGE_SIZE - (36 * RESIZE)),
                    (0, 660, 3 * (32 * RESIZE), IMAGE_SIZE - (36 * RESIZE)),
                    (192, 336, 4 * (32 * RESIZE), IMAGE_SIZE - (36 * RESIZE)),
                ]:
                    preview.paste(
                        source.crop((s_x, s_y, s_x + 32, s_y + 36)).resize(
                            (32 * RESIZE, 36 * RESIZE),
                            Resampling.NEAREST,
                        ),
                        (d_x, d_y)
                    )

            preview.save(folder + 'preview.png')



    def get_folder_name(self):
        return self.id

    def generate(self):
        folder = 'out/{0}/'.format(self.get_folder_name())

        shutil.rmtree(folder, True)
        os.mkdir(folder)
        os.mkdir(folder + 'graphics/')
        os.mkdir(folder + 'graphics/images')
        for s in sprite_sheet.sheets:
            s.label(self.bind.actions, folder + 'graphics/' + s.path, self.show_hotkeys)

        self.generate_preview(folder)

        if self.changes_hotkeys:
            with open(folder + 'interface.txt', "w", encoding='utf-8') as file:
                file.write(self.bind.express())

        with open(folder + 'info.txt', 'w', encoding='CP437') as file:
            file.write(self.generate_info_txt())

        with open(folder + 'steam_description.txt', 'w', encoding='utf-8') as file:
            file.write("\n".join(self.generate_description()))

        for f in [
            'graphics_building_icons_tweaks.txt',
            'graphics_interface_tweaks.txt',
            'tile_page_interface_tweaks.txt',
        ]:
            shutil.copy('ref/' + f, folder + 'graphics/' + f)

