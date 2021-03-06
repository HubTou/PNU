# ECHOBOX(1)

## NAME
echobox - write arguments in a box to the standard output

## SYNOPSIS
**echobox**
[-a\|--align name]
[-b\|--basic-char char]
[-d\|--debug]
[-f\|--fill-char char]
[-h\|--help\|-?]
[-i\|--inter-lines number]
[-S\|--style name]
[-s\|--spaces number]
[-t\|--trail-lines number]
[-v\|--version]
[--]
[string ...]

## DESCRIPTION
The **echobox** utility writes any specified operands, separated by single blank (' ') characters and followed by a newline ('\\n') character, in a box, to the standard output.

## OPTIONS

Options | Use
------- | ---
-a\|--align name|Sets the alignment to use. Possible values: left (default), center, middle, right.
-b\|--basic-char char|Sets the character to use with the basic style. Default value: '#'.
-d\|--debug|Enable debug level messages.
-f\|--fill-char char|Sets the character to use to fill the box. Default value: ' '.
-h\|--help\|-?|Print usage and a short help message and exit.
-i\|--inter-lines number|Sets the number of lines separating the text from the box on the top and bottom sides. Default value: 1.
-S\|--style name|Sets the style to use. Possible values: basic (default), ascii, single, curved, hatched, double, block.
-s\|--spaces number|Sets the number of spaces separating the text from the box on the left and right sides. Default value: 3.
-t\|--trail-lines number|Sets the number of blank lines following the box. Default value: 1.
-v\|--version|Print version and exit.
--|Options processing terminator. Contrarily to the [echo(1)](https://www.freebsd.org/cgi/man.cgi?query=echo) command, it is recognized as such.

## ENVIRONMENT
Environment variables are processed first and thus overridden by command line options.

Variable | Use
-------- | ---
ECHOBOX_STYLE | Sets the style to use.
ECHOBOX_ALIGN | Sets the alignment to use.
ECHOBOX_BASIC_CHAR | Sets the character to use with the basic style.
ECHOBOX_FILL_CHAR | Sets the character to use to fill the box.
ECHOBOX_SPACES | Sets the number of spaces separating the text from the box on the left and right sides.
ECHOBOX_INTER_LINES | Sets the number of lines separating the text from the box on the top and bottom sides.
ECHOBOX_TRAIL_LINES | Sets the number of blank lines following the box.
ECHOBOX_DEBUG | Enable debug level messages.
COLUMNS | Defines the number of columns in the terminal window. This variable is sometimes provided by the [Bash](http://www.gnu.org/software/bash/) shell and some others, but not necessarily exported. It's used for center and right alignments. Default value: 80.

## EXIT STATUS
The echobox utility exits 0 on success, and >0 if an error occurs.

## SEE ALSO
[dialog(1)](https://www.freebsd.org/cgi/man.cgi?query=dialog)

https://en.wikipedia.org/wiki/Box-drawing_character

https://unicode-table.com/fr/#box-drawing

## BUGS
Specifying a basic or fill [Unicode](https://home.unicode.org/) characters is not currently possible with the environment and command line options.

## STANDARDS
The echobox command is not a standard [UNIX](https://en.wikipedia.org/wiki/Unix)/[POSIX](https://en.wikipedia.org/wiki/POSIX) command.

It tries to follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for [Python](https://www.python.org/) code.
We check this with the [Pylint](https://www.pylint.org/) command.

## PORTABILITY
Tested under Windows, though the [hatched and curved Unicode characters](https://unicode-table.com/fr/#box-drawing) are not fully recognized in the cmd.exe and PowerShell command prompts.

## HISTORY
The echobox command was created as an example for the [PNU project](https://github.com/HubTou/PNU), demonstrating how to process the environment and the command line, and use the [Python logging module](https://docs.python.org/3/library/logging.html).

## LICENSE
This utility is available under the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

## AUTHOR
[Hubert Tournier](https://github.com/HubTou)

