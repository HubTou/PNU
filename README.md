# PNU / PyNIX
The PNU Project (PNU as in "PNU is Not Unix"):

(Yet another collection of) UNIX tools rewritten in Python, forming a kind of PyNIX.

It's meant to be pronounced "Pneu" (tyre in French), a "pun" which seems appropriate as it's clearly another reinvention of the wheel, longtime after the GNU project :-)

Objectives:
- Firstly intended as a learning exercise in Python/Unix for my son
- Eventually having some handy portable Unix tools, for example for Windows

Project status:
- This is a placeholder for publishing unix tools rewrites made by or with my son

Suggested tasks and progression:

Level 0 sub projects (super easy ones, string handling only):
- basename, dirname
- echo
- line
- true, false

Level 1 sub projects (easy ones, using basic math or data structures):
- banner
- factor, primes
- rot13 (non standard, check https://en.wikipedia.org/wiki/ROT13 or https://www.freebsd.org/cgi/man.cgi?query=rot13), caesar

Level 2 sub projects (easy ones, introducing command line options):
- cat
- cmp
- comm
- head
- sleep
- tail
- uniq
- wc => a good one to start with

Level 3 sub projects (easy ones, introducing system-level programming)
- chown, chgrp
- cp, ln, mv
- df
- dircmp
- du
- env
- id
- logname
- machid
- mkdir
- pwd
- rm, rmdir
- split
- sum (hint: use readily available libraries)
- touch
- uname

Level 4 sub projects (intermediate level, more complex parsing):
- cut

Level 5 sub projects (intermediate level, full blown commands):
- date
- ls
- tree (non standard) -> the one we started with!
- nl
- od

Pre-requisites:
- All commands need to be PEP 8 compliant (checked with pylint or see https://www.python.org/dev/peps/pep-0008/).
- Provide a script for testing the new command against the installed one
- Test execution under Windows
