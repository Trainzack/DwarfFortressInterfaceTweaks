import constants
changelog = {
    (1, 4): (
        "2022-12-13",
        "Arena Update",
        [
            "DF 0.50.03"
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