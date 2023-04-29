from sprite_sheet import building, main


class Action:

    """Represents a key that we have an interest in changing, and some information about what that key does. """

    def __init__(self, tag: str, ui_name: str, sprite_sheet=None, location=None,
                 arrow=None, location_active=None):
        self.tag = tag

        self.ui_name = ui_name
        self.sprite_sheet = sprite_sheet
        # Where on the spritesheet the sprite represting this action is, in tiles
        self.location = location
        self.location_active = location_active
        # Text representing whether there should be an arrow (left, right) in the text of this action
        self.arrow = arrow

        # Whether bindings that trigger this action should convert according to keyboard layout
        self.convert = True

        self.bindings = []

    def register_binding(self, binding):
        self.bindings.append(binding)

    def get_ui_text(self):
        out = "/".join([
            i for b in self.bindings
                for i in b.get_ui()
        ])
        align = 'normal'

        if self.arrow == "left":
            out = "←{0}".format(out)
            align = 'left'
        elif self.arrow == "right":
            out = "{0}→".format(out)
            align = 'right'

        return align, out


def get_actions():
    return [
        Action(
            tag='CURSOR_UP',
            ui_name='Cursor Up',
        ),
        Action(
            tag='CURSOR_DOWN',
            ui_name='Cursor Down',
        ),
        Action(
            tag='CURSOR_LEFT',
            ui_name='Cursor Left',
        ),
        Action(
            tag='CURSOR_RIGHT',
            ui_name='Cursor Right',
        ),
        Action(
            tag='CURSOR_UP_FAST',
            ui_name='Cursor Up Fast',
        ),
        Action(
            tag='CURSOR_DOWN_FAST',
            ui_name='Cursor Down Fast',
        ),
        Action(
            tag='CURSOR_LEFT_FAST',
            ui_name='Cursor Left Fast',
        ),
        Action(
            tag='CURSOR_RIGHT_FAST',
            ui_name='Cursor Right Fast',
        ),
        Action(
            tag='CURSOR_UP_Z',
            ui_name='Cursor Up Z',
        ),
        Action(
            tag='CURSOR_DOWN_Z',
            ui_name='Cursor Down Z',
        ),
        Action(
            tag='CURSOR_UP_Z_FAST',
            ui_name='Cursor Up Z Fast',
        ),
        Action(
            tag='CURSOR_DOWN_Z_FAST',
            ui_name='Cursor Down Z Fast',
        ),
        Action(
            tag='HOTKEY_BUILDING_ARMORSTAND',
            ui_name='Build Armorstand',
            sprite_sheet=building,
            location=(5, 11),
        ),
        Action(
            tag='HOTKEY_BUILDING_BED',
            ui_name='Build Bed',
            sprite_sheet=building,
            location=(0, 5),
        ),
        Action(
            tag='HOTKEY_BUILDING_CHAIR',
            ui_name='Build Chair',
            sprite_sheet=building,
            location=(1, 5),
        ),
        Action(
            tag='HOTKEY_BUILDING_COFFIN',
            ui_name='Build Coffin',
            sprite_sheet=building,
            location=(5, 5),
        ),
        Action(
            tag='HOTKEY_BUILDING_DOOR',
            ui_name='Build Door',
            sprite_sheet=building,
            location=(5, 6),
        ),
        Action(
            tag='HOTKEY_BUILDING_FLOODGATE',
            ui_name='Build Floodgate',
            sprite_sheet=building,
            location=(2, 9),
        ),
        Action(
            tag='HOTKEY_BUILDING_HATCH',
            ui_name='Build Hatch',
            sprite_sheet=building,
            location=(6, 6),
        ),
        Action(
            tag='HOTKEY_BUILDING_GRATE_WALL',
            ui_name='Build Wall Grate',
            sprite_sheet=building,
            location=(7, 7),
        ),
        Action(
            tag='HOTKEY_BUILDING_GRATE_FLOOR',
            ui_name='Build Floor Grate',
            sprite_sheet=building,
            location=(0, 8),
        ),
        Action(
            tag='HOTKEY_BUILDING_BARS_VERTICAL',
            ui_name='Build Vertical Bars',
            sprite_sheet=building,
            location=(1, 8),
        ),
        Action(
            tag='HOTKEY_BUILDING_BARS_FLOOR',
            ui_name='Build Floor Bars',
            sprite_sheet=building,
            location=(2, 8),
        ),
        Action(
            tag='HOTKEY_BUILDING_CABINET',
            ui_name='Build Cabinet',
            sprite_sheet=building,
            location=(4, 5),
        ),
        Action(
            tag='HOTKEY_BUILDING_BOX',
            ui_name='Build Chest',
            sprite_sheet=building,
            location=(3, 5),
        ),
        Action(
            tag='HOTKEY_BUILDING_KENNEL',
            ui_name='Build Vermin Catcher''s Shop',
            sprite_sheet=building,
            location=(5, 4),
        ),
        Action(
            tag='HOTKEY_BUILDING_FARMPLOT',
            ui_name='Build Farm Plot',
            sprite_sheet=building,
            location=(5, 3),
        ),
        Action(
            tag='HOTKEY_BUILDING_WEAPONRACK',
            ui_name='Build Weaponrack',
            sprite_sheet=building,
            location=(4, 11),
        ),
        Action(
            tag='HOTKEY_BUILDING_STATUE',
            ui_name='Build Statue',
            sprite_sheet=building,
            location=(7, 5),
        ),
        Action(
            tag='HOTKEY_BUILDING_TABLE',
            ui_name='Build Table',
            sprite_sheet=building,
            location=(2, 5),
        ),
        Action(
            tag='HOTKEY_BUILDING_ROAD_DIRT',
            ui_name='Build Dirt Road',
            sprite_sheet=building,
            location=(5, 7),
        ),
        Action(
            tag='HOTKEY_BUILDING_ROAD_PAVED',
            ui_name='Build Paved Road',
            sprite_sheet=building,
            location=(4, 7),
        ),
        Action(
            tag='HOTKEY_BUILDING_BRIDGE',
            ui_name='Build Bridge',
            sprite_sheet=building,
            location=(3, 7),
        ),
        Action(
            tag='HOTKEY_BUILDING_WELL',
            ui_name='Build Well',
            sprite_sheet=building,
            location=(1, 9),
        ),
        Action(
            tag='HOTKEY_BUILDING_WINDOW_GLASS',
            ui_name='Build Glass Window',
            sprite_sheet=building,
            location=(3, 8),
        ),
        Action(
            tag='HOTKEY_BUILDING_WINDOW_GEM',
            ui_name='Build Gem Window',
            sprite_sheet=building,
            location=(4, 8),
        ),
        Action(
            tag='HOTKEY_BUILDING_ANIMALTRAP',
            ui_name='Build Animal Trap',
            sprite_sheet=building,
            location=(5, 10),
        ),
        Action(
            tag='HOTKEY_BUILDING_CHAIN',
            ui_name='Build Chain',
            sprite_sheet=building,
            location=(3, 10),
        ),
        Action(
            tag='HOTKEY_BUILDING_CAGE',
            ui_name='Build Cage',
            sprite_sheet=building,
            location=(4, 10),
        ),
        Action(
            tag='HOTKEY_BUILDING_TRADEDEPOT',
            ui_name='Build Trade Depot',
            sprite_sheet=building,
            location=(0, 1),
        ),
        Action(
            tag='HOTKEY_BUILDING_TRAP',
            ui_name='Build Traps',
            sprite_sheet=building,
            location=(6, 0),
        ),
        Action(
            tag='HOTKEY_BUILDING_MACHINE',
            ui_name='Build Machines/Fluids',
            sprite_sheet=building,
            location=(4, 0),
        ),
        Action(
            tag='HOTKEY_BUILDING_INSTRUMENT',
            ui_name='Build Instrument',
            sprite_sheet=building,
            location=(4, 6),
        ),
        Action(
            tag='HOTKEY_BUILDING_SUPPORT',
            ui_name='Build Support',
            sprite_sheet=building,
            location=(5, 8),
        ),
        Action(
            tag='HOTKEY_BUILDING_ARCHERYTARGET',
            ui_name='Build Archery Target',
            sprite_sheet=building,
            location=(3, 11),
        ),
        Action(
            tag='HOTKEY_BUILDING_TRACTION_BENCH',
            ui_name='Build Traction Bench',
            sprite_sheet=building,
            location=(0, 6),
        ),
        Action(
            tag='HOTKEY_BUILDING_SLAB',
            ui_name='Build Slab',
            sprite_sheet=building,
            location=(6, 5),
        ),
        Action(
            tag='HOTKEY_BUILDING_NEST_BOX',
            ui_name='Build Nest Box',
            sprite_sheet=building,
            location=(6, 4),
        ),
        Action(
            tag='HOTKEY_BUILDING_BOOKCASE',
            ui_name='Build Bookcase',
            sprite_sheet=building,
            location=(1, 6),
        ),
        Action(
            tag='HOTKEY_BUILDING_HIVE',
            ui_name='Build Hive',
            sprite_sheet=building,
            location=(7, 4),
        ),
        Action(
            tag='HOTKEY_BUILDING_DISPLAY_FURNITURE',
            ui_name='Build Display Furniture',
            sprite_sheet=building,
            location=(2, 6),
        ),
        Action(
            tag='HOTKEY_BUILDING_OFFERING_PLACE',
            ui_name='Build Offering Place',
            sprite_sheet=building,
            location=(3, 6),
        ),
        Action(
            tag='HOTKEY_BUILDING_FURNITURE',
            ui_name='Build Furniture',
            sprite_sheet=building,
            location=(1, 0),
        ),
        Action(
            tag='HOTKEY_BUILDING_PORTALS',
            ui_name='Build Portals',
            sprite_sheet=building,
            location=(2, 0),
        ),
        Action(
            tag='HOTKEY_BUILDING_CAGES_CHAINS',
            ui_name='Build Cages Chains',
            sprite_sheet=building,
            location=(5, 0),
        ),
        Action(
            tag='HOTKEY_BUILDING_MILITARY',
            ui_name='Build Military',
            sprite_sheet=building,
            location=(7, 0),
        ),
        Action(
            tag='HOTKEY_BUILDING_MACHINE_SCREW_PUMP',
            ui_name='Build Screw Pump',
            sprite_sheet=building,
            location=(3, 9),
        ),
        Action(
            tag='HOTKEY_BUILDING_MACHINE_WATER_WHEEL',
            ui_name='Build Water Wheel',
            sprite_sheet=building,
            location=(4, 9),
        ),
        Action(
            tag='HOTKEY_BUILDING_MACHINE_WINDMILL',
            ui_name='Build Windmill',
            sprite_sheet=building,
            location=(5, 9),
        ),
        Action(
            tag='HOTKEY_BUILDING_MACHINE_GEAR_ASSEMBLY',
            ui_name='Build Gear Assembly',
            sprite_sheet=building,
            location=(6, 9),
        ),
        Action(
            tag='HOTKEY_BUILDING_MACHINE_AXLE_VERTICAL',
            ui_name='Build Vertical Axle',
            sprite_sheet=building,
            location=(0, 10),
        ),
        Action(
            tag='HOTKEY_BUILDING_MACHINE_AXLE_HORIZONTAL',
            ui_name='Build Horizontal Axle ',
            sprite_sheet=building,
            location=(7, 9),
        ),
        Action(
            tag='HOTKEY_BUILDING_MACHINE_ROLLERS',
            ui_name='Build Rollers',
            sprite_sheet=building,
            location=(2, 10),
        ),
        Action(
            tag='HOTKEY_BUILDING_SIEGEENGINE_BALLISTA',
            ui_name='Build Ballista',
            sprite_sheet=building,
            location=(6, 11),
        ),
        Action(
            tag='HOTKEY_BUILDING_SIEGEENGINE_CATAPULT',
            ui_name='Build Catapult',
            sprite_sheet=building,
            location=(7, 11),
        ),
        Action(
            tag='HOTKEY_BUILDING_TRAP_STONE',
            ui_name='Build Stonefall Trap',
            sprite_sheet=building,
            location=(7, 10),
        ),
        Action(
            tag='HOTKEY_BUILDING_TRAP_WEAPON',
            ui_name='Build Weapon Trap',
            sprite_sheet=building,
            location=(0, 11),
        ),
        Action(
            tag='HOTKEY_BUILDING_TRAP_LEVER',
            ui_name='Build Lever',
            sprite_sheet=building,
            location=(0, 9),
        ),
        Action(
            tag='HOTKEY_BUILDING_TRAP_TRIGGER',
            ui_name='Build Pressure Plate',
            sprite_sheet=building,
            location=(6, 10),
        ),
        Action(
            tag='HOTKEY_BUILDING_TRAP_CAGE',
            ui_name='Build Cage Trap',
            sprite_sheet=building,
            location=(1, 11),
        ),
        Action(
            tag='HOTKEY_BUILDING_TRAP_SPIKE',
            ui_name='Build Spike Trap',
            sprite_sheet=building,
            location=(2, 11),
        ),
        Action(
            tag='HOTKEY_BUILDING_CONSTRUCTION',
            ui_name='Build Construction',
            sprite_sheet=building,
            location=(3, 0),
        ),
        Action(
            tag='HOTKEY_BUILDING_CONSTRUCTION_WALL',
            ui_name='Build Wall',
            sprite_sheet=building,
            location=(7, 6),
        ),
        Action(
            tag='HOTKEY_BUILDING_CONSTRUCTION_FLOOR',
            ui_name='Build Floor',
            sprite_sheet=building,
            location=(0, 7),
        ),
        Action(
            tag='HOTKEY_BUILDING_CONSTRUCTION_RAMP',
            ui_name='Build Ramp',
            sprite_sheet=building,
            location=(1, 7),
        ),
        Action(
            tag='HOTKEY_BUILDING_CONSTRUCTION_STAIR_UPDOWN',
            ui_name='Build Stairs',
            sprite_sheet=building,
            location=(2, 7),
        ),
        Action(
            tag='HOTKEY_BUILDING_CONSTRUCTION_FORTIFICATION',
            ui_name='Build Fortifications',
            sprite_sheet=building,
            location=(6, 7),
        ),
        Action(
            tag='HOTKEY_BUILDING_CONSTRUCTION_TRACK',
            ui_name='Build Track',
            sprite_sheet=building,
            location=(6, 8),
        ),
        Action(
            tag='HOTKEY_BUILDING_CONSTRUCTION_TRACK_STOP',
            ui_name='Build Track Stop',
            sprite_sheet=building,
            location=(7, 8),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP',
            ui_name='Build Workshops',
            sprite_sheet=building,
            location=(0, 0),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOPS_CLOTHING_LEATHER',
            ui_name='Build Textiles Workshops',
            sprite_sheet=building,
            location=(7, 1),
        ),
        Action(
            tag='HOTKEY_BUILDING_FARMING',
            ui_name='Build Farming Workshops',
            sprite_sheet=building,
            location=(0, 2),
        ),
        Action(
            tag='HOTKEY_BUILDING_FURNACE',
            ui_name='Build Furnaces',
            sprite_sheet=building,
            location=(4, 1),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_LEATHER',
            ui_name="Build Leatherworker's Shop",
            sprite_sheet=building,
            location=(1, 3),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_QUERN',
            ui_name='Build Quern',
            sprite_sheet=building,
            location=(4, 4),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_MILLSTONE',
            ui_name='Build Millstone',
            sprite_sheet=building,
            location=(1, 10),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_LOOM',
            ui_name='Build Loom',
            sprite_sheet=building,
            location=(2, 3),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_CLOTHES',
            ui_name="Build Clothesmaker's Shop",
            sprite_sheet=building,
            location=(3, 3),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_BOWYER',
            ui_name="Build Bowyer's Workshop",
            sprite_sheet=building,
            location=(1, 2),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_CARPENTER',
            ui_name="Build Carpenter's Workshop",
            sprite_sheet=building,
            location=(1, 1),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_METALSMITH',
            ui_name='Build Forge',
            sprite_sheet=building,
            location=(3, 1),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_LAVAMILL',
            ui_name='Build Magma Forge',
            sprite_sheet=building,
            location=(3, 1),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_JEWELER',
            ui_name="Build Jeweler's Workshop",
            sprite_sheet=building,
            location=(6, 1),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_MASON',
            ui_name="Build Stoneworker Workshop",
            sprite_sheet=building,
            location=(2, 1),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_BUTCHER',
            ui_name='Build Butcher',
            sprite_sheet=building,
            location=(7, 3),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_TANNER',
            ui_name='Build Tanner',
            sprite_sheet=building,
            location=(0, 4),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_DYER',
            ui_name='Build Dyer',
            sprite_sheet=building,
            location=(4, 3),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_CRAFTSMAN',
            ui_name='Build Craftsman',
            sprite_sheet=building,
            location=(5, 1),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_SIEGE',
            ui_name='Build Siege Workshop',
            sprite_sheet=building,
            location=(3, 2),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_MECHANIC',
            ui_name='Build Mechanic',
            sprite_sheet=building,
            location=(2, 2),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_STILL',
            ui_name='Build Still',
            sprite_sheet=building,
            location=(6, 3),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_FARMER',
            ui_name="Build Farmer's Workshop",
            sprite_sheet=building,
            location=(3, 4),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_KITCHEN',
            ui_name='Build Kitchen',
            sprite_sheet=building,
            location=(2, 4),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_FISHERY',
            ui_name='Build Fishery',
            sprite_sheet=building,
            location=(1, 4),
        ),
        Action(
            tag='HOTKEY_BUILDING_WORKSHOP_ASHERY',
            ui_name='Build Ashery',
            sprite_sheet=building,
            location=(4, 2),
        ),
        Action(
            tag='HOTKEY_BUILDING_FURNACE_WOOD',
            ui_name='Build Wood Furnace',
            sprite_sheet=building,
            location=(5, 2),
        ),
        Action(
            tag='HOTKEY_BUILDING_FURNACE_SMELTER',
            ui_name='Build Smelter',
            sprite_sheet=building,
            location=(6, 2),
        ),
        Action(
            tag='HOTKEY_BUILDING_FURNACE_SMELTER_LAVA',
            ui_name='Build Magma Smelter',
            sprite_sheet=building,
            location=(6, 2),
        ),
        Action(
            tag='HOTKEY_BUILDING_FURNACE_GLASS',
            ui_name='Build Glass Furnace',
            sprite_sheet=building,
            location=(7, 2),
        ),
        Action(
            tag='HOTKEY_BUILDING_FURNACE_GLASS_LAVA',
            ui_name='Build Magma Glass Furnace',
            sprite_sheet=building,
            location=(7, 2),
        ),
        Action(
            tag='HOTKEY_BUILDING_FURNACE_KILN',
            ui_name='Build Kiln',
            sprite_sheet=building,
            location=(0, 3),
        ),
        Action(
            tag='HOTKEY_BUILDING_FURNACE_KILN_LAVA',
            ui_name='Build Magma Kiln',
            sprite_sheet=building,
            location=(0, 3),
        ),
        Action(
            tag='D_TOGGLE_RAMP_INDICATORS',
            ui_name='Toggle Ramp Indicators',
        ),
        Action(
            tag='D_TOGGLE_FLUID_NUMBERS',
            ui_name='Toggle Fluid Numbers',
        ),
        Action(
            tag='D_DESIGNATE_DIG',
            ui_name='Open Designate Dig Menu',
            sprite_sheet=main,
            location=(0, 1),
        ),
        Action(
            tag='D_DESIGNATE_CHOP',
            ui_name='Open Designate Chop Menu',
            sprite_sheet=main,
            location=(0, 12),
        ),
        Action(
            tag='D_DESIGNATE_GATHER',
            ui_name='Open Designate Gather Menu',
            sprite_sheet=main,
            location=(2, 12),
        ),
        Action(
            tag='D_DESIGNATE_SMOOTH',
            ui_name='Open Designate Smooth Menu',
            sprite_sheet=main,
            location=(0, 13),  # Or 2 13?
        ),
        Action(
            tag='D_DESIGNATE_ITEMS',
            ui_name='Open Designate Items Menu',
            sprite_sheet=main,
            location=(6, 11),
        ),
        Action(
            tag='D_DESIGNATE_TRAFFIC',
            ui_name='Open Designate Traffic Menu',
            sprite_sheet=main,
            location=(4, 1),
        ),
        Action(
            tag='D_DESIGNATE_ERASE',
            ui_name='Open Designate Erase Menu',
            sprite_sheet=main,
            location=(6, 4),
        ),
        Action(
            tag='DESIGNATE_DIG',
            ui_name='Designate Dig',
            sprite_sheet=main,
            location=(0, 2),
            location_active=(1, 2),
        ),
        Action(
            tag='DESIGNATE_STAIR_UPDOWN',
            ui_name='Designate Stair Updown',
            sprite_sheet=main,
            location=(2, 2),
            location_active=(3, 2),
        ),
        Action(
            tag='DESIGNATE_RAMP',
            ui_name='Designate Ramp',
            sprite_sheet=main,
            location=(0, 3),
            location_active=(1, 3),
        ),
        Action(
            tag='DESIGNATE_CHANNEL',
            ui_name='Designate Channel',
            sprite_sheet=main,
            location=(2, 3),
            location_active=(3, 3),
        ),
        Action(
            tag='DESIGNATE_DIG_REMOVE_STAIRS_RAMPS',
            ui_name='Designate Dig Remove Stairs Ramps',
            sprite_sheet=main,
            location=(0, 4),
            location_active=(1, 4)
        ),
        Action(
            tag='DESIGNATE_RECTANGLE',
            ui_name='Designate Rectangle',
            sprite_sheet=main,
            location=(3, 1),  # OR 9, 10
            location_active=(3, 4),  # OR 9 11
        ),
        Action(
            tag='DESIGNATE_FREE_DRAW',
            ui_name='Designate Free Draw',
            sprite_sheet=main,
            location=(2, 1),  # Or 8, 10
            location_active=(2, 4)  # OR 8, 11
        ),
        Action(
            tag='DESIGNATE_TOGGLE_ADVANCED_OPTIONS',
            ui_name='Designate Toggle Advanced Options',
            sprite_sheet=main,
            location=(2, 10),
            location_active=(3, 10)
        ),
        Action(
            tag='DESIGNATE_MINE_MODE_ALL',
            ui_name='Designate Mine Mode All',
            sprite_sheet=main,
            location=(0, 5),
            location_active=(1, 5),
        ),
        Action(
            tag='DESIGNATE_MINE_MODE_AUTO',
            ui_name='Designate Mine Mode Auto',
            sprite_sheet=main,
            location=(2, 5),
            location_active=(3, 5),
        ),
        Action(
            tag='DESIGNATE_MINE_MODE_ORE_GEM',
            ui_name='Designate Mine Mode Ore Gem',
            sprite_sheet=main,
            location=(0, 6),
            location_active=(1, 6),
        ),
        Action(
            tag='DESIGNATE_MINE_MODE_GEM',
            ui_name='Designate Mine Mode Gem',
            sprite_sheet=main,
            location=(2, 6),
            location_active=(3, 6),
        ),
        Action(
            tag='DESIGNATE_PRIORITY_UP',
            ui_name='Designate Priority Up',
            sprite_sheet=main,
            location=(0, 10),
            location_active=(1, 10),
            arrow='right',
        ),
        Action(
            tag='DESIGNATE_PRIORITY_DOWN',
            ui_name='Designate Priority Down',
            sprite_sheet=main,
            location=(0, 7),
            location_active=(1, 7),
            arrow='left',
        ),
        Action(
            tag='DESIGNATE_TOGGLE_MARKER',
            ui_name='Designate Toggle Blueprint',
            sprite_sheet=main,
            location=(0, 11),
            location_active=(1, 11),
        ),
        Action(
            tag='DESIGNATE_MARKER_TO_STANDARD',
            ui_name='Designate Blueprint To Standard',
            sprite_sheet=main,
            location=(4, 11),
            location_active=(5, 11),
        ),
        Action(
            tag='DESIGNATE_STANDARD_TO_MARKER',
            ui_name='Designate Standard To Blueprint',
            sprite_sheet=main,
            location=(2, 11),
            location_active=(3, 11),
        ),
        Action(
            tag='DESIGNATE_CHOP',
            ui_name='Designate Chop',
            sprite_sheet=main,
            location=(0, 12),
            location_active=(1, 12),
        ),
        Action(
            tag='DESIGNATE_PLANTS',
            ui_name='Designate Plants',
            sprite_sheet=main,
            location=(2, 12),
            location_active=(3, 12),
        ),
        Action(
            tag='DESIGNATE_SMOOTH',
            ui_name='Designate Smooth',
            sprite_sheet=main,
            location=(2, 13),
            location_active=(3, 13),
        ),
        Action(
            tag='DESIGNATE_ENGRAVE',
            ui_name='Designate Engrave',
            sprite_sheet=main,
            location=(0, 14),
            location_active=(1, 14),
        ),
        Action(
            tag='DESIGNATE_TRACK',
            ui_name='Designate Track',
            sprite_sheet=main,
            location=(8, 14),
            location_active=(9, 14)
        ),
        Action(
            tag='DESIGNATE_FORTIFY',
            ui_name='Designate Fortifications',
            sprite_sheet=main,
            location=(2, 14),
            location_active=(3, 14)
        ),
        Action(
            tag='DESIGNATE_CLAIM',
            ui_name='Designate Claim',
            sprite_sheet=main,
            location=(4, 10),
            location_active=(5, 10),
        ),
        Action(
            tag='DESIGNATE_UNCLAIM',
            ui_name='Designate Unclaim',
            sprite_sheet=main,
            location=(6, 10),
            location_active=(7, 10),
        ),
        Action(
            tag='DESIGNATE_MELT',
            ui_name='Designate Melt',
            sprite_sheet=main,
            location=(4, 13),
            location_active=(5, 13),
        ),
        Action(
            tag='DESIGNATE_NO_MELT',
            ui_name='Designate No Melt',
            sprite_sheet=main,
            location=(6, 13),
            location_active=(7, 13)
        ),
        Action(
            tag='DESIGNATE_DUMP',
            ui_name='Designate Dump',
            sprite_sheet=main,
            location=(4, 12),
            location_active=(5, 12),
        ),
        Action(
            tag='DESIGNATE_NO_DUMP',
            ui_name='Designate No Dump',
            sprite_sheet=main,
            location=(6, 12),
            location_active=(7, 12),
        ),
        Action(
            tag='DESIGNATE_HIDE',
            ui_name='Designate Hide',
            sprite_sheet=main,
            location=(6, 14),
            location_active=(7, 14),
        ),
        Action(
            tag='DESIGNATE_NO_HIDE',
            ui_name='Designate No Hide',
            sprite_sheet=main,
            location=(4, 14),
            location_active=(5, 14),
        ),
        Action(
            tag='DESIGNATE_TRAFFIC_HIGH',
            ui_name='Designate Traffic High',
            sprite_sheet=main,
            location=(4, 2),
            location_active=(5, 2)
        ),
        Action(
            tag='DESIGNATE_TRAFFIC_NORMAL',
            ui_name='Designate Traffic Normal',
            sprite_sheet=main,
            location=(6, 2),
            location_active=(7, 2),
        ),
        Action(
            tag='DESIGNATE_TRAFFIC_LOW',
            ui_name='Designate Traffic Low',
            sprite_sheet=main,
            location=(4, 3),
            location_active=(5, 3),
        ),
        Action(
            tag='DESIGNATE_TRAFFIC_RESTRICTED',
            ui_name='Designate Traffic Restricted',
            sprite_sheet=main,
            location=(6, 3),
            location_active=(7, 3),
        ),
        Action(
            tag='D_BUILDING',
            ui_name='Open Building Menu',
            sprite_sheet=main,
            location=(4, 5),
            location_active=(5, 5),
        ),
        Action(
            tag='D_STOCKPILES',
            ui_name='Open Stockpile Menu',
            sprite_sheet=main,
            location=(4, 6),
            location_active=(5, 6),
        ),
        Action(
            tag='D_CIVZONE',
            ui_name='Open Zones Menu',
            sprite_sheet=main,
            location=(4, 7),
            location_active=(5, 7),
        ),
        Action(
            tag='D_BURROWS',
            ui_name='Open Burrows Menu',
            sprite_sheet=main,
            location=(4, 8),
            location_active=(5, 8),
        ),
        Action(
            tag='D_HAULING',
            ui_name='Open Hauling Menu',
            sprite_sheet=main,
            location=(4, 9),
            location_active=(5, 9),
        ),
        Action(
            tag='D_UNITLIST',
            ui_name='Open Units Screen',
            sprite_sheet=main,
            location=(8, 2),
            location_active=(10, 10),
        ),
        Action(
            tag='D_JOBLIST',
            ui_name='Open Tasks Screen',
            sprite_sheet=main,
            location=(9, 2),
            location_active=(11, 10),
        ),
        Action(
            tag='D_LOCATIONS',
            ui_name='Open Locations Screen',
            sprite_sheet=main,
            location=(10, 2),
            location_active=(12, 10),
        ),
        Action(
            tag='D_LABOR',
            ui_name='Open Labor Screen',
            sprite_sheet=main,
            location=(8, 3),
            location_active=(10, 11),
        ),
        Action(
            tag='D_ORDERS',
            ui_name='Open Orders Screen',
            sprite_sheet=main,
            location=(6, 1),
            location_active=(11, 12),
        ),
        Action(
            tag='D_NOBLES',
            ui_name='Open Nobles Screen',
            sprite_sheet=main,
            location=(9, 3),
            location_active=(11, 11),
        ),
        Action(
            tag='D_ARTLIST',
            ui_name='Open Objects Screen',
            sprite_sheet=main,
            location=(10, 3),
            location_active=(12, 11),
        ),
        Action(
            tag='D_SQUADS',
            ui_name='Open Squads Menu',
            sprite_sheet=main,
            location=(6, 0),
        ),
        Action(
            tag='D_WORLD',
            ui_name='Open World Screen',
            sprite_sheet=main,
            location=(7, 0),
        ),
        Action(
            tag='D_JUSTICE',
            ui_name='Open Justice Screen',
            sprite_sheet=main,
            location=(8, 4),
            location_active=(10, 12),
        ),
        Action(
            tag='D_STOCKS',
            ui_name='Open Stocks Screen',
        ),
    ]
