# ![PNU logo](/_images/pnu-logo-small.png) The PNU project / PyNIX 
PNU as in "PNU is Not Unix": yet another collection of [UNIX](https://en.wikipedia.org/wiki/Unix) tools rewritten in [Python](https://www.python.org/), forming a kind of PyNIX.

It's meant to be pronounced "Pneu" (tyre in French), a "pun" which seems appropriate as it's clearly another reinvention of the wheel, longtime after the [GNU project](https://www.gnu.org/gnu/thegnuproject.en.html) :-)

## Objectives:
* Firstly intended as a learning exercise in Python/Unix for my son, but open to anyone.
* Eventually having some handy portable Unix tools, for example for Windows.

## Project status:
* The project is ongoing.
* This place is a placeholder for publishing unix tools rewrites made by or with my son, or others.

## Suggested tasks and progression:
A long term goal would be to have all the [utilities](https://pubs.opengroup.org/onlinepubs/9699919799/idx/utilities.html) included in [POSIX.1](https://pubs.opengroup.org/onlinepubs/9699919799/nframe.html), most utilities sitting under /bin and /usr/bin, some common non-standard utilities, as well as some utilities of our own.

The following, [D&D](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons) inspired, level structure is proposed for gamification. It would also be fun to set level bosses and associated trophies.

The [Python Standard Library](https://docs.python.org/3/library/index.html) documentation and the online book [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) could be useful to progress quickly.

### Level 0 sub projects (super easy ones)
Handling return codes, printing & reading to/from the terminal, and basic string handling:
* [true](https://www.freebsd.org/cgi/man.cgi?query=true), [false](https://www.freebsd.org/cgi/man.cgi?query=false)
* [yes](https://www.freebsd.org/cgi/man.cgi?query=yes)
* [echo](https://www.freebsd.org/cgi/man.cgi?query=echo) => without options for a start
* [basename, dirname](https://www.freebsd.org/cgi/man.cgi?query=basename) => without options for a start

### Level 1 sub projects (easy ones)
Basic math or data structures, school level:
* [factor, primes](https://www.freebsd.org/cgi/man.cgi?query=factor)

### Level 2 sub projects (easy ones)
Basic command line & environment processing, file operations and filters:
* [echobox](https://github.com/HubTou/PNU/tree/main/echobox) => check this already made full example first
* [wc](https://www.freebsd.org/cgi/man.cgi?query=wc)

### Level 3 sub projects (easy ones)
Basic system utilities:

### Level 4 sub projects (easy ones)

### Level 5 sub projects (intermediate ones):
Regular expressions, text parsing:

CSV, JSON, XML, HTML data handling:

Intermediate system utilities:

### Level 10 sub projects (advanced ones):
Advanced system utilities:

Office documents manipulation, image manipulation, web scraping, network applications, automation

### Level 15 sub projects (master-level ones):
Languages (interpreters, compilers), database management systems, network stacks, operating systems, device drivers:

## Pre-requisites:
* All commands need to be [PEP 8](https://www.python.org/dev/peps/pep-0008/) compliant (which you can check with [pylint](https://www.pylint.org/)).
* Provide a script for testing the new command against the installed one
* Test execution under Windows
