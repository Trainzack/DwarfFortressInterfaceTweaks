import constants
changelog = {
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