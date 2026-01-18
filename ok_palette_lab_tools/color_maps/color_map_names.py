"""Get a list of all color map names."""


def get_general_color_map_names() -> list[str]:
    """Get a list of general color map names.

    Returns:
        A list of general color map names.
    """
    return [
        "autumn",
        "autumn_wide",
        "ocean",
        "ocean_wide",
        "forest",
        "forest_wide",
        "red",
        "red_wide",
        "purple_green_yellow",
        "tea",
    ]


def get_diverging_color_map_names() -> list[str]:
    """Get a list of diverging color map names.

    Returns:
        A list of diverging color map names.
    """
    return [
        "blue_brown_white",
        "blue_brown_white_wide",
        "blue_brown_light",
        "blue_brown_light_wide",
        "blue_red_white",
        "blue_red_white_wide",
        "blue_red_light",
        "blue_red_light_wide",
        "rainbow",
    ]
