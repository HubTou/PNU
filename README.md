# ![PNU logo](/_images/pnu-logo-small.png) The PNU project / PyNIX 
PNU, as in "PNU is Not Unix", is yet another collection of [UNIX](https://en.wikipedia.org/wiki/Unix) tools rewritten in [Python](https://www.python.org/), forming a kind of PyNIX.

It's meant to be pronounced "Pneu" (tyre in French), a "pun" which seems appropriate as it's clearly another reinvention of the [wheel](http://www.catb.org/jargon/html/W/wheel.html), longtime after the [GNU project](https://www.gnu.org/gnu/thegnuproject.en.html) :-)

## Objectives:
* Firstly intended as a [learning exercise](https://github.com/topics/learning-exercise) in Python/Unix for my son, but open to anyone.
* Passing on some Unix culture & lore to a generation of [new hackers](http://www.catb.org/~esr/jargon/) (in the [original and noble meaning of the word](http://www.catb.org/~esr/jargon/html/H/hacker.html)).
* Having some handy portable Unix tools, for example for Windows (though there are [plenty of other solutions](https://github.com/HubTou/PNU/wiki/Wilderness-Survival-Guide) for that).
* Ultimately to have most of the relevant [standard utilities](https://pubs.opengroup.org/onlinepubs/9699919799/idx/utilities.html) included in [POSIX.1](https://pubs.opengroup.org/onlinepubs/9699919799/nframe.html) (around 80 utilities, about 50% of the set), many utilities sitting under /bin and /usr/bin in a [BSD](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)/[GNU Linux](https://en.wikipedia.org/wiki/Linux) system, some usual non-standard utilities, as well as some utilities of our own.

## Project status:
* The project is ongoing.
* This place is both for the challenge description and a placeholder for publishing unix tools rewrites made by contributors, though you can also just create:
  * your own Github repositories and link them to the project by using the [pnu-project](https://github.com/topics/pnu-project) topic
  * your own [PyPi](https://pypi.org/) packages and link them to the project by using the [pnu-project](https://pypi.org/search/?q=pnu-project) keyword

## How to contribute:
* Decide on a Unix command to reimplement in Python 3.x (see list below for suggestions).
* [Read the tutorials](https://github.com/HubTou/PNU/blob/main/_demos/README.md)
* [Read the guidelines for contribution](https://github.com/HubTou/PNU/wiki/The-Player's-Handbook)
* [Come discuss it with us on the forums](https://github.com/HubTou/PNU/discussions)

## Suggested tasks and progression:
The following, [(A)D&D](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons) inspired, [level structure](https://github.com/HubTou/PNU/discussions/2) is proposed for [gamification](https://en.wikipedia.org/wiki/Gamification).
We suggest level bosses in order to complete a level (but no [Demogorgon](https://en.wikipedia.org/wiki/Demogorgon#Dungeons_&_Dragons) here, we are not in [Stranger Things](https://en.wikipedia.org/wiki/Stranger_Things) :-)) and associated trophies for fun :-)

The commands below are linked to their latest [FreeBSD man page](https://www.freebsd.org/cgi/man.cgi) (the web site also gives access to a lot of other Unix-like operating systems versions), but you should probably start implementing their simpler (and more testing oriented) [POSIX.1 versions](https://pubs.opengroup.org/onlinepubs/9699919799/idx/utilities.html).

## Basic levels
### Level 1 sub projects
Handling return codes, printing to the terminal:
* [true](https://www.freebsd.org/cgi/man.cgi?query=true), [false](https://www.freebsd.org/cgi/man.cgi?query=false)
* [yes](https://www.freebsd.org/cgi/man.cgi?query=yes)
* [echo](https://www.freebsd.org/cgi/man.cgi?query=echo) => with hardcoded option for a start. Suggested level boss. Trophy: a dummy/teat.

### Level 2 sub projects
Basic [string handling](https://docs.python.org/3/library/string.html):
* [basename, dirname](https://www.freebsd.org/cgi/man.cgi?query=basename) => without options for a start (hint: there's a hidden shortcut)

Basic math or data structures, school level:
* [caesar, rot13](https://www.freebsd.org/cgi/man.cgi?query=caesar)
* [factor, primes](https://www.freebsd.org/cgi/man.cgi?query=factor) => suggested level boss. Trophy: a schoolbag.

### Level 3 sub projects
Basic [filters](https://github.com/HubTou/PNU/tree/main/_demos/gorgon), command line & [environment](https://www.freebsd.org/cgi/man.cgi?query=environ) processing, file operations:
* [echo](https://www.freebsd.org/cgi/man.cgi?query=echo) => with full options
* [basename](https://www.freebsd.org/cgi/man.cgi?query=basename) => with full options
* [read](https://www.freebsd.org/cgi/man.cgi?query=read) => careful with the environment as it won't be a Shell builtin command...
* [cat](https://www.freebsd.org/cgi/man.cgi?query=cat) => with POSIX options only for a start
* [head](https://www.freebsd.org/cgi/man.cgi?query=head)
* [expand, unexpand](https://www.freebsd.org/cgi/man.cgi?query=expand)
* [fold](https://www.freebsd.org/cgi/man.cgi?query=fold)
* [wc](https://www.freebsd.org/cgi/man.cgi?query=wc) => suggested level boss

### Level 4 sub projects
Basic text processing utilities, multiple files or many options:
* [cat](https://www.freebsd.org/cgi/man.cgi?query=cat) => with full options
* [nl](https://www.freebsd.org/cgi/man.cgi?query=nl)
* [cmp](https://www.freebsd.org/cgi/man.cgi?query=cmp)
* [comm](https://www.freebsd.org/cgi/man.cgi?query=comm)
* [uniq](https://www.freebsd.org/cgi/man.cgi?query=uniq) => suggested level boss

### Level 5 sub projects
Basic utilities using more complex parsing:
* [expr](https://www.freebsd.org/cgi/man.cgi?query=expr) => just a warmer
* [printf](https://www.freebsd.org/cgi/man.cgi?query=printf)
* [getopts](https://www.freebsd.org/cgi/man.cgi?query=getopts)
* [cut](https://www.freebsd.org/cgi/man.cgi?query=cut) => suggested level boss

## Intermediate levels
System utilities (implying minimum Unix system knowledge).
[Regular expressions](https://docs.python.org/3/library/re.html), text parsing.
[CSV](https://docs.python.org/3/library/csv.html), [JSON](https://docs.python.org/3/library/json.html), [XML](https://docs.python.org/3/library/xml.html), [HTML](https://docs.python.org/3/library/html.html) data handling.

### Level 6 sub projects
Basic system utilities (super easy ones):
* [pwd](https://www.freebsd.org/cgi/man.cgi?query=pwd)
* [pathchk](https://www.freebsd.org/cgi/man.cgi?query=pathchk)

Check this already made full example first to discover the system information Python knows about:
* [about](https://github.com/HubTou/about)

### Level 7 sub projects
Basic system utilities, possibly recursive ones:
* [chmod](https://www.freebsd.org/cgi/man.cgi?query=chmod)
* [chown](https://www.freebsd.org/cgi/man.cgi?query=chown)
* [chgrp](https://www.freebsd.org/cgi/man.cgi?query=chgrp)

### Level 8 sub projects
* [du](https://www.freebsd.org/cgi/man.cgi?query=du)

### Level 9 sub projects

### Level 10 sub projects
* [tree](http://mama.indstate.edu/users/ice/tree/) => Not standard but a pretty complete one for our purpose. Suggested level boss. Trophy: an oak tree

## Advanced levels
Office documents manipulation, image manipulation, web scraping, network applications, automation.

### Level 11 sub projects
Advanced system utilities, data compression:
* [compress, uncompress](https://www.freebsd.org/cgi/man.cgi?query=compress)
* [zcat](https://www.freebsd.org/cgi/man.cgi?query=zcat)

### Level 12 sub projects
Interactive full screen applications:
* [vi](https://www.freebsd.org/cgi/man.cgi?query=vi) => Suggested level boss

### Level 13 sub projects
### Level 14 sub projects
### Level 15 sub projects

## Master levels
Languages (interpreters, compilers), database management systems, network protocols:

### Level 16 sub projects
* [awk](https://www.freebsd.org/cgi/man.cgi?query=awk)

### Level 17 sub projects
### Level 18 sub projects
### Level 19 sub projects

### Level 20 sub projects
* [sh](https://www.freebsd.org/cgi/man.cgi?query=sh) => Suggested level boss. Trophy: a shell of course

## Immortal levels
It's a long way to the top if you wanna get your entry in the "Deities & [Demigods](http://www.catb.org/jargon/html/D/demigod.html)" of hackers, but here are some examples to inspire you from the [Unix & open source pantheon](https://www.facesofopensource.com/unix/) (note: having a [beard](http://jargonf.org/wiki/barbu) is not mandatory)

However, all of this is beyond the scope of the project and probably not a good idea to implement in Python :-)

### Demigods level transcending projects
Full operating system kernels & device drivers:
* Your own [Minix](https://en.wikipedia.org/wiki/Minix)/[386BSD](https://en.wikipedia.org/wiki/386BSD)/Linux like operating system with PNU userland utilities :-)

### Deities level transcending projects
Making your own hardware platform and all the software to run it.
* Although not Unix related, my own personal idol, [The Woz](https://en.wikipedia.org/wiki/Steve_Wozniak) springs to mind here and I recommend his excellent autobiography, [iWoz](https://en.wikipedia.org/wiki/IWoz), for a good glimpse into a true Hacker's mind.
