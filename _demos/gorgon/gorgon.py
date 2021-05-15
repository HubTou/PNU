#!/usr/bin/env python
""" gorgon - turn any input into stone
License: 3-clause BSD (see https://opensource.org/licenses/BSD-3-Clause)
Author: Hubert Tournier
"""

import sys

# Version string used by the what(1) and ident(1) commands:
ID = "@(#) $Id: gorgon - turn any input into stone v1.0.0 (May 14, 2021) by Hubert Tournier $"


def petrification(_):
    """Turns the input into stone"""
    return "stone"


for line in sys.stdin:
    for word in line.rstrip().split(" "):
        print(petrification(word) + " ", end="")
    print()

sys.exit(0)
