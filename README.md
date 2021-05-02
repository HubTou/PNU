# ![PNU logo](/_images/pnu-logo-small.png) The PNU project / PyNIX 
PNU as in "PNU is Not Unix": yet another collection of [UNIX](https://en.wikipedia.org/wiki/Unix) tools rewritten in [Python](https://www.python.org/), forming a kind of PyNIX.

It's meant to be pronounced "Pneu" (tyre in French), a "pun" which seems appropriate as it's clearly another reinvention of the wheel, longtime after the [GNU project](https://www.gnu.org/gnu/thegnuproject.en.html) :-)

## Objectives:
* Firstly intended as a learning exercise in Python/Unix for my son, but open to anyone.
* Having some handy portable Unix tools, for example for Windows.
* Ultimately to have all the relevant [standard utilities](https://pubs.opengroup.org/onlinepubs/9699919799/idx/utilities.html) included in [POSIX.1](https://pubs.opengroup.org/onlinepubs/9699919799/nframe.html), many utilities sitting under /bin and /usr/bin in a [BSD](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)/[GNU Linux](https://en.wikipedia.org/wiki/Linux) system, some usual non-standard utilities, as well as some utilities of our own.

## Project status:
* The project is ongoing.
* This place is both a challenge description and a placeholder for publishing unix tools rewrites made by or with my son, or others.

## How to contribute:
* Decide on a Unix command to reimplement in Python 3.x (see list below for suggestions).
* Aim to be [PEP 8](https://www.python.org/dev/peps/pep-0008/) compliant (which you can check with [pylint](https://www.pylint.org/)).
* Eventually, use [Black](https://github.com/psf/black), "The Uncompromising Code Formatter", to format your code in a standard way.

Ideally (but leave this for the future if it's too complicated for the time being):
* Provide a script for testing the new command against the installed one.
* Also test execution under Windows for the portability goal.
* Write some documentation in a README.md file (in [GitHub markdown](https://guides.github.com/features/mastering-markdown/)) or [man](https://www.freebsd.org/cgi/man.cgi?query=man)ual page (in the newer [mdoc](https://www.freebsd.org/cgi/man.cgi?query=mdoc&sektion=7) or classic [man](https://www.freebsd.org/cgi/man.cgi?query=man&sektion=7) languages).
* Write an installation script or Makefile.
* Select an [OSI-approved Open Source License](https://opensource.org/licenses) and put it in a License file.
* [Clone this repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) and submit your changes.

## Suggested tasks and progression:
The following, [D&D](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons) inspired, level structure is proposed for gamification.
It would also be fun to set level bosses and associated trophies :-)

The [Python Standard Library](https://docs.python.org/3/library/index.html) online documentation and the online book [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) could be useful to progress quickly.

The commands below are linked to their latest [FreeBSD man page](https://www.freebsd.org/cgi/man.cgi), which also gives access to a lot of other Unix-like operating systems versions, but you should probably start implementing their simpler (and more testing oriented) [POSIX.1 version}(https://pubs.opengroup.org/onlinepubs/9699919799/idx/utilities.html).

## Basic levels
### Level 0 sub projects (super easy ones)
Handling return codes, printing & reading to/from the terminal, and basic string handling:
* [basename, dirname](https://www.freebsd.org/cgi/man.cgi?query=basename) => without options for a start. Suggested level boss
* [echo](https://www.freebsd.org/cgi/man.cgi?query=echo) => without options for a start
* [true](https://www.freebsd.org/cgi/man.cgi?query=true), [false](https://www.freebsd.org/cgi/man.cgi?query=false)
* [yes](https://www.freebsd.org/cgi/man.cgi?query=yes)

### Level 1 sub projects (easy ones)
Basic math or data structures, school level:
* [factor, primes](https://www.freebsd.org/cgi/man.cgi?query=factor) => Suggested level boss

### Level 2 sub projects (easy ones)
Basic command line & environment processing, file operations and filters:
* [echobox](https://github.com/HubTou/PNU/tree/main/echobox) => Check this already made full example first
* [expand, unexpand](https://www.freebsd.org/cgi/man.cgi?query=expand)
* [fold](https://www.freebsd.org/cgi/man.cgi?query=fold)
* [head](https://www.freebsd.org/cgi/man.cgi?query=head)
* [read](https://www.freebsd.org/cgi/man.cgi?query=read) => Careful with the environment as it won't be a Shell builtin command...
* [wc](https://www.freebsd.org/cgi/man.cgi?query=wc) => Suggested level boss

### Level 3 sub projects (easy ones)
Basic text processing utilities, multiple files or many options:
* [cat](https://www.freebsd.org/cgi/man.cgi?query=cat) => Here because of the number of options
* [cmp](https://www.freebsd.org/cgi/man.cgi?query=cmp)
* [comm](https://www.freebsd.org/cgi/man.cgi?query=comm)
* [expr](https://www.freebsd.org/cgi/man.cgi?query=expr)
* [nl](https://www.freebsd.org/cgi/man.cgi?query=nl)
* [pathchk](https://www.freebsd.org/cgi/man.cgi?query=pathchk)
* [pwd](https://www.freebsd.org/cgi/man.cgi?query=pwd)
* [uniq](https://www.freebsd.org/cgi/man.cgi?query=uniq) => Suggested level boss

### Level 4 sub projects (easy ones)

## Intermediate levels
Regular expressions, text parsing.
CSV, JSON, XML, HTML data handling.

### Level 5 sub projects (intermediate ones):
Basic system utilities, possibly recursive:
* [chmod](https://www.freebsd.org/cgi/man.cgi?query=chmod)
* [chown](https://www.freebsd.org/cgi/man.cgi?query=chown)
* [chgrp](https://www.freebsd.org/cgi/man.cgi?query=chgrp)

### Level 6 sub projects (intermediate ones):
* [du](https://www.freebsd.org/cgi/man.cgi?query=du)

### Level 7 sub projects (intermediate ones):

### Level 8 sub projects (intermediate ones):

### Level 9 sub projects (intermediate ones):

## Advanced levels
Office documents manipulation, image manipulation, web scraping, network applications, automation.

### Level 10 sub projects (advanced ones):
Advanced system utilities:
* [compress](https://www.freebsd.org/cgi/man.cgi?query=compress)

### Level 14 sub projects (advanced ones):
Interactive full screen applications:
* [vi](https://www.freebsd.org/cgi/man.cgi?query=vi) => Suggested level boss

## Master levels
### Level 15 sub projects:
Languages (interpreters, compilers), database management systems, network protocols:
* [awk](https://www.freebsd.org/cgi/man.cgi?query=awk)
* [sh](https://www.freebsd.org/cgi/man.cgi?query=sh) => Suggested level boss

## Immortal levels
### Level transcending projects:
Full operating system kernels & device drivers:
* Your own [Minix](https://en.wikipedia.org/wiki/Minix)/[386BSD](https://en.wikipedia.org/wiki/386BSD)/Linux like operating system with PNU userland utilities :-)
