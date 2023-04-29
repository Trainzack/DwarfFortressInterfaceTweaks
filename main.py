import os
import shutil

from PIL import Image

import action
import bindings
import constants
import keyboard_layout
import sprite_sheet
from mod import Mod


def main():
    #old = bindings.Bindings('ref/interface_default.txt', action.get_actions())

    mods = [
        Mod(
            name='Interface Tweaks',
            id='interface_tweaks',
            keyboard_layout=keyboard_layout.QWERTY,
            hotkey_path='ref/interface_default.txt',
            steam_id=2899720701,
            image_path='ref/interface_tweaks_preview.png',
        ),
        Mod(
            name='Interface Tweaks (Without Hotkey Hints)',
            id='interface_tweaks_hotkeyless',
            keyboard_layout=keyboard_layout.QWERTY,
            hotkey_path='ref/interface_default.txt',
            steam_id=2901961781,
            show_hotkeys=False,
            tagline='Without Hotkey Hints',
            color=(49, 44, 52),
            description="A set of minor interface tweaks, like a squad disband button that isn't confusing. This "
                        "version doesn't have the hotkey hints, so you can change them to your heart's content. ",
        ),
        Mod(
            name='Ergonomic Hotkeys (QWERTY)',
            id='ergonomic_hotkeys_qwerty',
            keyboard_layout=keyboard_layout.QWERTY,
            hotkey_path='ref/interface_new.txt',
            steam_id=2901375133,
        ),
        Mod(
            name='Ergonomic Hotkeys (QWERTZ)',
            id='ergonomic_hotkeys_qwertz',
            keyboard_layout=keyboard_layout.QWERTZ,
            hotkey_path='ref/interface_new.txt',
            steam_id=2901375168,
        ),
        Mod(
            name='Ergonomic Hotkeys (AZERTY)',
            id='ergonomic_hotkeys_azerty',
            keyboard_layout=keyboard_layout.AZERTY,
            hotkey_path='ref/interface_new.txt',
            steam_id=2901375200,
        ),
        Mod(
            name='Ergonomic Hotkeys (Dvorak)',
            id='ergonomic_hotkeys_dvorak',
            keyboard_layout=keyboard_layout.DVORAK,
            hotkey_path='ref/interface_new.txt',
            steam_id=2901375224,
        ),
        Mod(
            name='Ergonomic Hotkeys (Colemak)',
            id='ergonomic_hotkeys_colemak',
            keyboard_layout=keyboard_layout.COLEMAK,
            hotkey_path='ref/interface_new.txt',
            steam_id=2901960067,
        ),
        Mod(
            name='Ergonomic Hotkeys (Workman)',
            id='ergonomic_hotkeys_workman',
            keyboard_layout=keyboard_layout.WORKMAN,
            hotkey_path='ref/interface_new.txt',
            steam_id=2901960027,
        ),
        Mod(
            name='Ergonomic Hotkeys (Neo)',
            id='ergonomic_hotkeys_neo',
            keyboard_layout=keyboard_layout.NEO2,
            hotkey_path='ref/interface_new.txt',
            steam_id=2903051534,
        ),
    ]

    shutil.rmtree('out/', True)
    os.mkdir('out/')
    for mod in mods:
        mod.generate()
        dest = constants.PATH_DF_INSTALLATION + 'mods/' + mod.get_folder_name()
        shutil.rmtree(dest, True)
        shutil.copytree('out/' + mod.get_folder_name(), dest)

    print('Created {0} mods.'.format(len(mods)))


if __name__ == '__main__':
    main()
