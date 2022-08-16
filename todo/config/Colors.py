from enum import Enum
from todo.Task import State as TaskState
from todo.Project import State as ProjectState


class TextColors(Enum):
    """All the colors that can be printed in the terminal"""

    # No Color
    NoC = "\033[0m"

    # Foreground Color
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Purple = "\033[35m"
    Cyan = "\033[36m"
    White = "\033[37m"

    # Background Color
    On_Black = "\033[40m"
    On_Red = "\033[41m"
    On_Green = "\033[42m"
    On_Yellow = "\033[43m"
    On_Blue = "\033[44m"
    On_Purple = "\033[45m"
    On_Cyan = "\033[46m"
    On_White = "\033[47m"

    # Special
    Bold = "\033[1m"


class ColorTable:
    """A table to translate configuration options and states to a color from
    TextColors"""

    def __init__(self):
        """Initialize the color table so that every state will print with 'No
        Color'. This will ensure that even if there is no color configuration
        read from the configuration file, everything will still run."""

        task_configs = [
            "task_" + s.lower() for s in TaskState.__members__.keys()
        ]
        project_configs = [
            "project_" + s.lower() for s in ProjectState.__members__.keys()
        ]
        self.color_dict = dict.fromkeys(
            task_configs + project_configs,
            TextColors.NoC.value,
        )
        self.NoC = TextColors.NoC.value

    def import_config(self, color_config):
        """Set colors according to the config file. The config being passed to
        this method is just the 'Colors' section of the config"""

        for state in self.color_dict.keys():
            if state in color_config:
                self.color_dict[state] = self.determine_color(
                    color_config[state]
                )

    def determine_color(self, color):
        """From a string that matches a color from TextColors, return the
        corresponding color code."""

        color_string = ""
        for c in color.split(", "):
            if c in TextColors.__members__.keys():
                color_string += TextColors[c].value
        return color_string
