#!/usr/bin/env python
""" echobox - write arguments in a box to the standard output
License: 3-clause BSD (see https://opensource.org/licenses/BSD-3-Clause)
Author: Hubert Tournier
"""

import getopt
import logging
import os
import sys

NAME = "echobox"

# Version string used by the what(1) and ident(1) commands:
ID = "@(#) $Id: echobox - write arguments in a box v1.1.0 (May 9, 2021) by Hubert Tournier $"

# Cf. https://en.wikipedia.org/wiki/Box-drawing_character
# Cf. https://unicode-table.com/fr/#box-drawing
STYLES = {
    "basic": {
        "Upper left corner": "#",
        "Horizontal line": "#",
        "Upper right corner": "#",
        "Vertical line": "#",
        "Lower left corner": "#",
        "Lower right corner": "#",
    },
    "ascii": {
        "Upper left corner": "+",
        "Horizontal line": "-",
        "Upper right corner": "+",
        "Vertical line": "|",
        "Lower left corner": "+",
        "Lower right corner": "+",
    },
    "single": {
        "Upper left corner": "\u250c",
        "Horizontal line": "\u2500",
        "Upper right corner": "\u2510",
        "Vertical line": "\u2502",
        "Lower left corner": "\u2514",
        "Lower right corner": "\u2518",
    },
    "curved": {
        "Upper left corner": "\u256d",
        "Horizontal line": "\u2500",
        "Upper right corner": "\u256e",
        "Vertical line": "\u2502",
        "Lower left corner": "\u2570",
        "Lower right corner": "\u256f",
    },
    "hatched": {
        "Upper left corner": "\u250f",
        "Horizontal line": "\u2501",
        "Upper right corner": "\u2513",
        "Vertical line": "\u2503",
        "Lower left corner": "\u2517",
        "Lower right corner": "\u251b",
    },
    "double": {
        "Upper left corner": "\u2554",
        "Horizontal line": "\u2550",
        "Upper right corner": "\u2557",
        "Vertical line": "\u2551",
        "Lower left corner": "\u255a",
        "Lower right corner": "\u255d",
    },
    "block": {
        "Upper left corner": "\u2588",
        "Horizontal line": "\u2588",
        "Upper right corner": "\u2588",
        "Vertical line": "\u2588",
        "Lower left corner": "\u2588",
        "Lower right corner": "\u2588",
    },
}

# default parameters. Can be overcome by environment variables, then command line options
parameters = {
    "Style": "basic",
    "Alignment": "left",
    "Basic char": "#",
    "Fill char": " ",
    "Surrounding spaces": 3,
    "Internal lines": 1,
    "Trailing lines": 1,
}

################################################################################
def display_help():
    """Displays usage and help"""
    print()
    print("usage: %s [-a|--align name] [-b|--basic-char char] [-d|--debug]" % NAME)
    print("       [-f|--fill-char char] [-h|--help|-?] [-i|--inter-lines number]")
    print("       [-S|--style name] [-s|--spaces number] [-t|--trail-lines number]")
    print("       [-v|--version] [--] [string ...]")
    print("  ----------------   ---------------------------------------------------")
    print(
        "  -a|--align         Box alignment (left, middle, center, right): %s"
        % parameters["Alignment"]
    )
    print(
        "  -b|--basic-char    Character to use for basic style: '%s'"
        % parameters["Basic char"]
    )
    print("  -d|--debug         Enable debug mode")
    print(
        "  -f|--fill-char     Character to use to fill background: '%s'"
        % parameters["Fill char"]
    )
    print("  -h|--help|-?       Print usage and this help message and exit")
    print(
        "  -i|--inter-lines   Blank lines around the text: %d"
        % parameters["Internal lines"]
    )
    print("  -S|--style         Style to use: %s" % parameters["Style"])
    print(
        "  -s|--spaces        Spaces around the text: %d"
        % parameters["Surrounding spaces"]
    )
    print(
        "  -t|--trail-lines   Blank lines after the box: %d"
        % parameters["Trailing lines"]
    )
    print("  -v|--version       Print version and exit")
    print("  --                 Options processing terminator")
    print()
    print("Available styles: " + " ".join(STYLES.keys()))
    print()


################################################################################
def process_environment_variables():
    """Process environment variables"""
    # pylint: disable=C0103
    global parameters, columns
    # pylint: enable=C0103

    if "ECHOBOX_STYLE" in os.environ.keys():
        if os.environ["ECHOBOX_STYLE"] in STYLES.keys():
            parameters["Style"] = os.environ["ECHOBOX_STYLE"]
        else:
            logging.error("Unknown style in the ECHOBOX_STYLE environment variable")
            parameters["Style"] = "basic"

    if "ECHOBOX_ALIGN" in os.environ.keys():
        if os.environ["ECHOBOX_ALIGN"].lower() in ("center", "middle"):
            parameters["Alignment"] = "center"
        elif os.environ["ECHOBOX_ALIGN"].lower() == "left":
            parameters["Alignment"] = "left"
        elif os.environ["ECHOBOX_ALIGN"].lower() == "right":
            parameters["Alignment"] = "right"
        else:
            logging.error("Unknown alignment in the ECHOBOX_ALIGN environment variable")
            parameters["Alignment"] = "left"

    if (
        "ECHOBOX_BASIC_CHAR" in os.environ.keys()
        and len(os.environ["ECHOBOX_BASIC_CHAR"]) == 1
    ):
        parameters["Basic char"] = os.environ["ECHOBOX_BASIC_CHAR"]
        STYLES["basic"]["Upper left corner"] = parameters["Basic char"]
        STYLES["basic"]["Horizontal line"] = parameters["Basic char"]
        STYLES["basic"]["Upper right corner"] = parameters["Basic char"]
        STYLES["basic"]["Vertical line"] = parameters["Basic char"]
        STYLES["basic"]["Lower left corner"] = parameters["Basic char"]
        STYLES["basic"]["Lower right corner"] = parameters["Basic char"]

    if (
        "ECHOBOX_FILL_CHAR" in os.environ.keys()
        and len(os.environ["ECHOBOX_FILL_CHAR"]) == 1
    ):
        parameters["Fill char"] = os.environ["ECHOBOX_FILL_CHAR"]

    if "ECHOBOX_SPACES" in os.environ.keys():
        if os.environ["ECHOBOX_SPACES"].isdigit():
            parameters["Surrounding spaces"] = int(os.environ["ECHOBOX_SPACES"])
        else:
            logging.error(
                "Non numeric value in the ECHOBOX_SPACES environment variable"
            )

    if "ECHOBOX_INTER_LINES" in os.environ.keys():
        if os.environ["ECHOBOX_INTER_LINES"].isdigit():
            parameters["Internal lines"] = int(os.environ["ECHOBOX_INTER_LINES"])
        else:
            logging.error(
                "Non numeric value in the ECHOBOX_INTER_LINES environment variable"
            )

    if "ECHOBOX_TRAIL_LINES" in os.environ.keys():
        if os.environ["ECHOBOX_TRAIL_LINES"].isdigit():
            parameters["Trailing lines"] = int(os.environ["ECHOBOX_TRAIL_LINES"])
        else:
            logging.error(
                "Non numeric value in the ECHOBOX_TRAIL_LINES environment variable"
            )

    if "ECHOBOX_DEBUG" in os.environ.keys():
        logging.disable(logging.NOTSET)

    # The following environment variable is provided by the Bash shell and some others,
    # but not necessarily exported:
    if "COLUMNS" in os.environ.keys() and os.environ["COLUMNS"].isdigit():
        columns = int(os.environ["COLUMNS"])


################################################################################
def process_command_line():
    """Process command line"""
    # pylint: disable=C0103
    global parameters
    # pylint: enable=C0103

    try:
        # option letters followed by : expect an argument
        # same for option strings followed by =
        options, remaining_arguments = getopt.getopt(
            sys.argv[1:],
            "a:b:df:hi:S:s:t:v?",
            [
                "align=",
                "basic-char=",
                "debug",
                "fill-char=",
                "help",
                "inter-lines=",
                "style=",
                "spaces=",
                "trail-lines=",
                "version",
            ],
        )
    except getopt.GetoptError as error:
        logging.critical("Syntax error: %s", error)
        display_help()
        sys.exit(1)

    for option, argument in options:

        if option in ("-a", "--align"):
            if argument.lower() in ("left", "center", "middle", "right"):
                parameters["Alignment"] = argument.lower()
            else:
                logging.critical(
                    "-a/--align parameter must be one of: left, middle, center, right"
                )
                sys.exit(1)

        elif option in ("-b", "--basic-char"):
            if len(argument) == 1:
                parameters["Basic char"] = argument
                STYLES["basic"]["Upper left corner"] = parameters["Basic char"]
                STYLES["basic"]["Horizontal line"] = parameters["Basic char"]
                STYLES["basic"]["Upper right corner"] = parameters["Basic char"]
                STYLES["basic"]["Vertical line"] = parameters["Basic char"]
                STYLES["basic"]["Lower left corner"] = parameters["Basic char"]
                STYLES["basic"]["Lower right corner"] = parameters["Basic char"]
            else:
                logging.critical("-b/--basic-char parameter must be a single character")
                sys.exit(1)

        elif option in ("-d", "--debug"):
            logging.disable(logging.NOTSET)

        elif option in ("-f", "--fill-char"):
            if len(argument) == 1:
                parameters["Fill char"] = argument
            else:
                logging.critical("-f/--fill-char parameter must be a single character")
                sys.exit(1)

        elif option in ("-h", "--help", "-?"):
            display_help()
            sys.exit(0)

        elif option in ("-i", "--inter-lines"):
            if argument.isdigit() and int(argument) >= 0:
                parameters["Internal lines"] = int(argument)
            else:
                logging.critical(
                    "-i/--inter-lines parameter must be a positive integer"
                )
                sys.exit(1)

        elif option in ("-S", "--style"):
            if argument.lower() in STYLES.keys():
                parameters["Style"] = argument.lower()
            else:
                logging.critical(
                    "-S/--style parameter must be one of: %s", " ".join(STYLES.keys())
                )
                sys.exit(1)

        elif option in ("-s", "--spaces"):
            if argument.isdigit() and int(argument) >= 0:
                parameters["Surrounding spaces"] = int(argument)
            else:
                logging.critical("-s/--spaces parameter must be a positive integer")
                sys.exit(1)

        elif option in ("-t", "--trail-lines"):
            if argument.isdigit() and int(argument) >= 0:
                parameters["Trailing lines"] = int(argument)
            else:
                logging.critical(
                    "-t/--trail-lines parameter must be a positive integer"
                )
                sys.exit(1)

        elif option in ("-v", "--version"):
            print(ID.replace("@(#) $Id: ", "").replace(" $", ""))
            sys.exit(0)

    return remaining_arguments


################################################################################
def print_indentation():
    """Prints indentation spaces"""
    for _ in range(text_indent):
        print(" ", end="")


################################################################################
def print_upper_box_line():
    """Prints the upper box line"""
    print_indentation()
    print(STYLES[parameters["Style"]]["Upper left corner"], end="")
    for _ in range(text_width_with_spaces):
        print(STYLES[parameters["Style"]]["Horizontal line"], end="")
    print(STYLES[parameters["Style"]]["Upper right corner"])


################################################################################
def print_inter_lines():
    """Prints inner box lines if requested"""
    for _ in range(parameters["Internal lines"]):
        print_indentation()
        print(STYLES[parameters["Style"]]["Vertical line"], end="")
        for _ in range(text_width_with_spaces):
            print(parameters["Fill char"], end="")
        print(STYLES[parameters["Style"]]["Vertical line"])


################################################################################
def print_text_line():
    """Prints the text in an inner box line"""
    print_indentation()
    print(STYLES[parameters["Style"]]["Vertical line"], end="")
    for _ in range(parameters["Surrounding spaces"]):
        print(parameters["Fill char"], end="")
    print(text, end="")
    for _ in range(parameters["Surrounding spaces"]):
        print(parameters["Fill char"], end="")
    print(STYLES[parameters["Style"]]["Vertical line"])


################################################################################
def print_lower_box_line():
    """Prints the lower box line"""
    print_indentation()
    print(STYLES[parameters["Style"]]["Lower left corner"], end="")
    for _ in range(text_width_with_spaces):
        print(STYLES[parameters["Style"]]["Horizontal line"], end="")
    print(STYLES[parameters["Style"]]["Lower right corner"])


################################################################################
def print_blank_lines():
    """Prints blank lines if requested"""
    for _ in range(parameters["Trailing lines"]):
        print()


################################################################################
logging.basicConfig(
    level=logging.DEBUG, format="%(module)s: %(levelname)s: %(message)s"
)
logging.disable(logging.DEBUG)

# pylint: disable=C0103
columns = 80
process_environment_variables()
arguments = process_command_line()
text = " ".join(arguments)

text_width_with_spaces = len(text) + 2 * parameters["Surrounding spaces"]
if parameters["Alignment"] == "left":
    text_indent = 0
elif parameters["Alignment"] == "right":
    text_indent = columns - 2 - text_width_with_spaces
else:
    text_indent = (columns - text_width_with_spaces) // 2
# pylint: enable=C0103

logging.debug(
    'style=%s align=%s basic="%s" fill="%s" spaces=%d inter-lines=%d trail-lines=%d',
    parameters["Style"],
    parameters["Alignment"],
    parameters["Basic char"],
    parameters["Fill char"],
    parameters["Surrounding spaces"],
    parameters["Internal lines"],
    parameters["Trailing lines"],
)
logging.debug(
    'text="%s" width=%d columns=%d indent=%d', text, len(text), columns, text_indent
)

print_upper_box_line()
print_inter_lines()
print_text_line()
print_inter_lines()
print_lower_box_line()
print_blank_lines()

sys.exit(0)
