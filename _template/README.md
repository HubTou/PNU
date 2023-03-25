# Installation
Once you have installed [Python](https://www.python.org/downloads/) and its packages manager [pip](https://pip.pypa.io/en/stable/installation/),
use one of the following commands, depending on if you want only this tool, the full set of PNU tools, or PNU plus a selection of additional third-parties tools:

```
pip install COMMAND
pip install PNU
pip install pytnix
```

# COMMAND(1)

## NAME
COMMAND - ONE LINE DESCRIPTION

## SYNOPSIS
**COMMAND**
\[--debug\]
\[--help|-?\]
\[--version\]
\[--\]

## DESCRIPTION
The **COMMAND** utility

### OPTIONS
Options | Use
------- | ---
--debug|Enable debug mode
--help\|-?|Print usage and a short help message and exit
--version|Print version and exit
--|Options processing terminator

## ENVIRONMENT
The COMMAND_DEBUG environment variable can be set to any value to enable debug mode.

The *FLAVOUR* or *COMMAND_FLAVOUR* environment variables can be set to one of the following values, to implement only the corresponding options and behaviours:
* posix : POSIX [COMMAND](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/COMMAND.html)
* unix | unix:v10 : Unix v10 [COMMAND(1)](http://man.cat-v.org/unix_10th/1/COMMAND)
* bsd | bsd:freebsd : FreeBSD [COMMAND(1)](https://www.freebsd.org/cgi/man.cgi?query=COMMAND)
* gnu | gnu:linux | linux : GNU/Linux [COMMAND(1)](https://man7.org/linux/man-pages/man1/COMMAND.1.html)
* plan9 : Plan 9 [COMMAND(1)](http://man.cat-v.org/plan_9/1/COMMAND)
* inferno : Inferno [COMMAND(1)](http://man.cat-v.org/inferno/1/COMMAND)

However, if the *POSIXLY_CORRECT* environment variable is set to any value, then the POSIX flavour will be selected.

## FILES

## EXIT STATUS
The **COMMAND** utility exits 0 on success, and >0 if an error occurs.

## EXAMPLES

## SEE ALSO
[OTHER_CMD(1)](https://www.freebsd.org/cgi/man.cgi?query=OTHER_CMD),
[OTHER_CMD_2(1)](https://www.freebsd.org/cgi/man.cgi?query=OTHER_CMD_2)

## STANDARDS
The **COMMAND** utility is a standard UNIX/POSIX command.
The **COMMAND** utility is a standard UNIX command, though not a POSIX one.
The **COMMAND** utility is not a standard UNIX command.

This re-implementation tries to follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for [Python](https://www.python.org/) code.

## PORTABILITY
To be tested under Windows.
Tested OK under Windows.

## HISTORY
This re-implementation was made for the [PNU project](https://github.com/HubTou/PNU).

## LICENSE
It is available under the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

## AUTHORS
[YOU](https://github.com/YOU)

This manual page is mainly based on the one written for [FreeBSD](https://www.freebsd.org/) by [HIM](https://github.com/HIM).

## CAVEATS

## BUGS

## SECURITY CONSIDERATIONS

