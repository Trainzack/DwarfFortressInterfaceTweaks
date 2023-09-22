# Thanks https://www.izscomic.com/2012/06/dwarf-fortress-ttf-font-download/

PATH_DF_INSTALLATION = "C:/Program Files (x86)/Steam/steamapps/common/Dwarf Fortress/"


MOD_NAME = "Ergonomic Hotkeys"


VERSION = (1, 6)

STEAM_TAGS = [
    "mod",
    "qol",
    "ui"
]
STEAM_METADATA = [
    "GNU Terry Pratchett"
]

def get_version_string(ver):
    return ".".join(str(v) for v in ver)

VERSION_STRING = get_version_string(VERSION)

def get_version_number(ver):
    return 133700000 + 100 * ver[0] + ver[1]


def get_earliest_compatible_version():
    return (VERSION[0], 0)
