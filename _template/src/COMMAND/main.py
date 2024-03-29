#!/usr/bin/env python3
""" COMMAND - ONE_LINE_DESCRIPTION
License: 3-clause BSD (see https://opensource.org/licenses/BSD-3-Clause)
Author: YOU
"""

import getopt
import logging
import os
import sys

import libpnu

# Version string used by the what(1) and ident(1) commands:
ID = "@(#) $Id: COMMAND - ONE_LINE_DESCRIPTION v1.0.0 (MONTH DAY, YEAR) by YOU $"

# Default parameters. Can be overcome by environment variables, then command line options
parameters = {
    "Command flavour": "PNU",
}


####################################################################################################
def _display_help():
    """ Display usage and help """
    #pylint: disable=C0301
    if parameters["Command flavour"] == "posix":
        # TODO: define subset of options here
        pass
    elif parameters["Command flavour"] in ("bsd", "bsd:freebsd"):
        # TODO: define subset of options here
        pass
    elif parameters["Command flavour"] in ("gnu", "gnu:linux", "linux"):
        # TODO: define subset of options here
        pass
    else: # PNU
        print("usage: COMMAND [--debug] [--help|-?] [--version]", file=sys.stderr)
        print("       [--] filename [...]", file=sys.stderr)
        print("  ------------------  --------------------------------------------------", file=sys.stderr)
        print("  --debug             Enable debug mode", file=sys.stderr)
        print("  --help|-?           Print usage and this help message and exit", file=sys.stderr)
        print("  --version           Print version and exit", file=sys.stderr)
        print("  --                  Options processing terminator", file=sys.stderr)
    print(file=sys.stderr)
    #pylint: enable=C0301


####################################################################################################
def _handle_interrupts(signal_number, current_stack_frame):
    """ Prevent SIGINT signals from displaying an ugly stack trace """
    print(" Interrupted!\n", file=sys.stderr)
    sys.exit(0)


####################################################################################################
def _process_environment_variables():
    """ Process environment variables """
    #pylint: disable=C0103, W0602
    global parameters
    #pylint: enable=C0103, W0602

    if "COMMAND_DEBUG" in os.environ:
        logging.disable(logging.NOTSET)

    if "FLAVOUR" in os.environ:
        parameters["Command flavour"] = os.environ["FLAVOUR"].lower()
    if "COMMAND_FLAVOUR" in os.environ:
        parameters["Command flavour"] = os.environ["COMMAND_FLAVOUR"].lower()

    # From "man environ":
    # POSIXLY_CORRECT
    # When set to any value, this environment variable
    # modifies the behaviour of certain commands to (mostly)
    # execute in a strictly POSIX-compliant manner.
    if "POSIXLY_CORRECT" in os.environ:
        parameters["Command flavour"] = "posix"

    # Command variants supported:
    if parameters["Command flavour"] == "posix":
        # TODO: define specific parameters here
        pass
    elif parameters["Command flavour"] in ("bsd", "bsd:freebsd"):
        # TODO: define specific parameters here
        pass
    elif parameters["Command flavour"] in ("gnu", "gnu:linux", "linux"):
        # TODO: define specific parameters here
        pass
    elif parameters["Command flavour"] == "PNU":
        pass
    else:
        logging.critical("Unimplemented command FLAVOUR: %s", parameters["Command flavour"])
        sys.exit(1)

    logging.debug("_process_environment_variables(): parameters:")
    logging.debug(parameters)


####################################################################################################
def _process_command_line():
    """ Process command line options """
    #pylint: disable=C0103, W0602
    global parameters
    #pylint: enable=C0103, W0602

    # option letters followed by : expect an argument
    # same for option strings followed by =
    if parameters["Command flavour"] == "posix":
        character_options = "?"
        string_options = [
            "debug",
            "help",
            "version",
        ]
    elif parameters["Command flavour"] in ("bsd", "bsd:freebsd"):
        character_options = "?"
        string_options = [
            "debug",
            "help",
            "version",
        ]
    elif parameters["Command flavour"] in ("gnu", "gnu:linux", "linux"):
        character_options = "?"
        string_options = [
            "debug",
            "help",
            "version",
        ]
    else: # PNU
        character_options = "?"
        string_options = [
            "debug",
            "help",
            "version",
        ]

    try:
        options, remaining_arguments = getopt.getopt(
            sys.argv[1:], character_options, string_options
        )
    except getopt.GetoptError as error:
        logging.critical("Syntax error: %s", error)
        _display_help()
        sys.exit(1)

    for option, argument in options:

        if option == "--debug":
            logging.disable(logging.NOTSET)

        elif option in ("--help", "-?"):
            _display_help()
            sys.exit(0)

        elif option == "--version":
            print(ID.replace("@(" + "#)" + " $" + "Id" + ": ", "").replace(" $", ""))
            sys.exit(0)

    logging.debug("_process_command_line(): parameters:")
    logging.debug(parameters)
    logging.debug("_process_command_line(): remaining_arguments:")
    logging.debug(remaining_arguments)

    return remaining_arguments


####################################################################################################
def main():
    """ The program's main entry point """
    program_name = os.path.basename(sys.argv[0])

    libpnu.initialize_debugging(program_name)
    libpnu.handle_interrupt_signals(_handle_interrupts)
    _process_environment_variables()
    arguments = _process_command_line()

    exit_status = 0
    for argument in arguments:
        # Do something with each remaining argument
        pass

    sys.exit(exit_status)


if __name__ == "__main__":
    main()
