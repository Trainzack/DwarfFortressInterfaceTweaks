import constants
changelog = {
    (1, 6): (
        "2023-09-19",
        "Notification Update",
        [
            "DF 0.50.10"
        ],
        [
            "Added notification screen button."
        ]
    ),
    (1, 5): (
        "2023-07",
        "Linux Compatibility Fix",
        [
            "DF 0.50.09"
        ],
        [
            "Fixed tile page reference with incorrect case, causing a crash on Linux."
        ]
    ),
    (1, 4): (
        "2023-07-18",
        "Arena Update",
        [
            "DF 0.50.09"
        ],
        [
            "Add arena UI elements",
            "Make designation priority numbers colored"
            "Set deletion icon of stockpiles, zones, burrows, and hauling routes to trash can"
        ]
    ),
    (1, 0): (
        "2022-12-13",
        "Initial Release",
        [
            "DF 0.50.03"
        ],
        [
        ]
    ),
}


def get_most_recent_changes():
    return [change for change in changelog[constants.VERSION][3]]