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

### Level 0 sub projects (super easy ones)
Handling return codes, printing & reading to/from the terminal, and basic string handling:
* [true](https://www.freebsd.org/cgi/man.cgi?query=true), [false](https://www.freebsd.org/cgi/man.cgi?query=false)
* [yes](https://www.freebsd.org/cgi/man.cgi?query=yes)
* [echo](https://www.freebsd.org/cgi/man.cgi?query=echo) => without options for a start
* [basename, dirname](https://www.freebsd.org/cgi/man.cgi?query=basename) => without options for a start

### Level 1 sub projects (easy ones)
Basic math or data structures, school level:
* [factor, primes](https://www.freebsd.org/cgi/man.cgi?query=factor)

### Level 2 sub projects (easy ones, introducing command line options):
* [echobox](https://github.com/HubTou/PNU/tree/main/echobox) => check this full example first for environment and command line processing
* [wc](https://www.freebsd.org/cgi/man.cgi?query=wc)

## Pre-requisites:
* All commands need to be [PEP 8](https://www.python.org/dev/peps/pep-0008/) compliant (which you can check with [pylint](https://www.pylint.org/)).
* Provide a script for testing the new command against the installed one
* Test execution under Windows
