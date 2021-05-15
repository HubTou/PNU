#!/usr/bin/env python
""" logging1 - logging basic example
License: 3-clause BSD (see https://opensource.org/licenses/BSD-3-Clause)
Author: Hubert Tournier
"""

import logging
import os
import sys

# Version string used by the what(1) and ident(1) commands:
ID = "@(#) $Id: logging1 - logging basic example v1.0.0 (May 15, 2021) by Hubert Tournier $"


def show_logging_levels():
    """Prints a message at each logging level"""
    logging.debug("Debug message (detailed diagnostic information)")
    logging.info("Info message (things working as expected)")
    logging.warning(
        "Warning message (things still working as expected, but potential for future errors)"
    )
    logging.error("Error message (unable to perform some function)")
    logging.critical("Critical message (program unable to continue)")


PROGRAM_NAME = os.path.basename(sys.argv[0])
CONSOLE_LOG_FORMAT = PROGRAM_NAME + ": %(levelname)s: %(message)s"
logging.basicConfig(format=CONSOLE_LOG_FORMAT, level=logging.DEBUG)
logging.disable(logging.INFO)

show_logging_levels()
print()

print("Now changing the logging level to DEBUG and above")
logging.disable(logging.NOTSET)

show_logging_levels()
print()

print("Some examples with parameters in error messages:")
ERROR_MESSAGE = "FMH!"
logging.error("Message: %s", ERROR_MESSAGE)
CRITICAL_ERROR_MESSAGE = "Fandango on core :-("
logging.critical("Message: %s", CRITICAL_ERROR_MESSAGE)

sys.exit(0)
