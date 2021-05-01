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

### Level 0 sub projects (super easy ones, string handling only):
* basename, dirname
* echo (without getopt for a start)
* line
* true, false

### Level 1 sub projects (easy ones, using basic math or data structures):
* [banner](https://www.freebsd.org/cgi/man.cgi?query=banner)
* [factor, primes](https://www.freebsd.org/cgi/man.cgi?query=factor)
* [caesar, rot13](https://www.freebsd.org/cgi/man.cgi?query=caesar) (non standard, check [Wikipedia](https://en.wikipedia.org/wiki/ROT13))

### Level 2 sub projects (easy ones, introducing command line options):
* [echobox](https://github.com/HubTou/PNU/tree/main/echobox) => check this full example first for environment and command line processing
* cat
* cmp
* comm
* head
* sleep
* tail
* uniq => a good one to start with
* wc => a good one to start with

### Level 3 sub projects (easy ones, introducing system-level programming)
* chown, chgrp
* cp, ln, mv
* df
* dircmp
* du
* env
* id
* logname
* machid
* mkdir
* pwd
* rm, rmdir
* split
* sum (hint: use readily available libraries)
* touch
* uname

### Level 4 sub projects (intermediate level, more complex parsing):
* cut

### Level 5 sub projects (intermediate level, full blown commands or bigger projects):
* date
* ls
* tree (non standard) -> the one we started with!
* nl
* od

## Pre-requisites:
* All commands need to be [PEP 8](https://www.python.org/dev/peps/pep-0008/) compliant (which you can check with [pylint](https://www.pylint.org/)).
* Provide a script for testing the new command against the installed one
* Test execution under Windows
