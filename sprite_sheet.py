from PIL import Image, ImageFont
from PIL import ImageDraw


class SpriteSheet:

    def __init__(self, tag, path, tile_size: tuple,
                 our_tile_size=None, start_pos=(0, 0)):

        self.tag = tag

        self.path = path

        self.image = Image.open(self.path)

        self.tile_size = tile_size

        self.our_tile_size = our_tile_size if our_tile_size else tile_size
        self.start_pos = start_pos

        self.page_dimension_pixels = (self.image.width, self.image.height)

    def express(self):
        out = [
            "[TILE_PAGE:{0}]".format(self.tag),
            "[FILE:{0}]".format(self.path),
            "[TILE_DIM:{0}]".format(":".join(
                [str(i) for i in self.tile_size]
            )),
            "[PAGE_DIM_PIXELS:{0}]".format(":".join(
                [str(i) for i in self.page_dimension_pixels]
            )),
        ]
        return "\n\t".join(out)

    def label(self, actions, destination, show_hotkeys=True):

        out = self.image.copy()
        if not show_hotkeys:
            out.save(destination)
            return

        draw = ImageDraw.Draw(out)
        font = ImageFont.truetype('ref/curses8x12.ttf', 12)
        #font = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 12)

        locations = dict()

        for a in actions:
            if a.sprite_sheet == self and a.location:
                align, text = a.get_ui_text()
                added_locations = [a.location]
                if a.location_active:
                    added_locations.append(a.location_active)

                for i in added_locations:
                    if i not in locations.keys():
                        locations[i] = (align, [text])
                    elif text not in locations[i][1]:
                        locations[i][1].append(text)


        for location, values in locations.items():
            align, texts = values
            ax, ay = location
            anchor = 'rs'

            text = "/".join(texts)

            if align == 'left':
                anchor = 'ls'

            x = ax * self.our_tile_size[0] + self.start_pos[0]
            y = ay * self.our_tile_size[1] + self.start_pos[1]
            if align == 'left':
                x += 2
            elif align == 'right' or len(text) > 1:
                x += (self.our_tile_size[0] - 2)
            else:
                x += (self.our_tile_size[0] - 4)
            y += (self.our_tile_size[0] - 4)
            # shadow
            for dx, dy in [
                (x-1, y), (x+1, y), (x, y-1), (x, y+1)
            ]:
                draw.text((dx, dy), text, font=font, fill=(0, 0, 0, 255), anchor=anchor)
            draw.text((x, y), text, font=font, fill=(255, 255, 255, 255), anchor=anchor)

        out.save(destination)

main = SpriteSheet(
    'INTERFACE_BITS_TWEAKED', 'images/interface_bits_tweaked.png', (8, 12),
    our_tile_size=(32, 36), start_pos=(0, 196),

)
building = SpriteSheet('BUILDING_ICONS_TWEAKED', 'images/building_icons_tweaked.png', (32, 32))
squad = SpriteSheet('SQUAD_DISBAND', 'images/squad_disband.png', (8, 12))
arena = SpriteSheet('INTERFACE_BITS_ARENA_TWEAKED', 'images/interface_bits_arena_tweaked.png',
                    (8, 12), our_tile_size=(32, 36), start_pos=(0,4))
announcements = SpriteSheet('INTERFACE_BITS_ANNOUNCEMENTS_TWEAKED', 'images/interface_bits_announcements_tweaked.png',
                    (8, 12), our_tile_size=(24, 36), start_pos=(1,12))

sheets = [
    main,
    squad,
    building,
    arena,
    announcements,
]