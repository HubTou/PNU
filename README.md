# ![PNU logo](https://github.com/HubTou/PNU/blob/main/_images/pnu-logo-and-title-small.png)
PNU, as in [PNU is Not Unix](http://www.catb.org/jargon/html/R/recursive-acronym.html), is a challenge project and a learning exercise to reimplement [UNIX](https://en.wikipedia.org/wiki/Unix) command-line tools in [Python](https://www.python.org/), forming a kind of "[pytnix](https://github.com/HubTou/pytnix)" portable user-land utilities collection.

It's meant to be pronounced "Pneu" (tyre in French), a "pun" which seems appropriate as it's clearly another reinvention of the [wheel](http://www.catb.org/jargon/html/W/wheel.html), longtime after the [GNU project](https://www.gnu.org/gnu/thegnuproject.en.html) :-)

## Objectives:
* Originally intended as a [learning exercise](https://github.com/topics/learning-exercise) in Python/Unix for my son, but open to anyone.
* Passing on some Unix culture & lore to a generation of [new hackers](http://www.catb.org/~esr/jargon/) (in the [original and noble meaning of the word](http://www.catb.org/~esr/jargon/html/H/hacker.html)).
* Having some handy portable Unix tools, for example for Windows (though there are [plenty of other solutions](https://github.com/HubTou/PNU/wiki/Wilderness-Survival-Guide) for that).
* Ultimately to have most of the relevant [standard utilities](https://pubs.opengroup.org/onlinepubs/9699919799/idx/utilities.html) included in [POSIX.1](https://pubs.opengroup.org/onlinepubs/9699919799/nframe.html), many utilities sitting under /bin and /usr/bin in a modern [BSD](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)/[GNU Linux](https://en.wikipedia.org/wiki/Linux) system, some usual non-standard utilities, as well as some utilities of our own.

## Project status:
* The project is ongoing. You can install [what's available](https://github.com/HubTou/PNU/releases/latest) from [our package](https://pypi.org/project/PNU/) with the following console command:
```Shell
pip install PNU
```
or you can install PNU plus a selection of additional third-parties tools with this command:
```Shell
pip install pytnix
```
* This page is both for the challenge description and for referencing unix tools rewrites made by contributors.
* To contribute you can simply create:
  * your own Github repositories and link them to the project by using the [pnu-project](https://github.com/topics/pnu-project) topic
  * your own [PyPi](https://pypi.org/) packages and link them to the project by using the [pnu-project](https://pypi.org/search/?q=pnu-project) keyword (but please don't use the "pnu-" package prefix for your own entries)

## How to contribute:
* As a player:
  * Decide on a Unix command to reimplement in Python 3.x (see list below for suggestions or our [Master / targets list](https://github.com/HubTou/PNU/wiki/The-Monster-Manual) for full details).
  * [Read the tutorials](https://github.com/HubTou/PNU/blob/main/_demos/README.md)
  * [Read the guidelines for contribution](https://github.com/HubTou/PNU/wiki/The-Player's-Handbook) (among other [documentation manuals](https://github.com/HubTou/PNU/wiki))
  * [Come discuss it with us on the forums](https://github.com/HubTou/PNU/discussions)
* As an organizer:
  * [Read the guidelines for organization](https://github.com/HubTou/PNU/wiki/Dungeon-Master's-Guide)

## Suggested tasks and progression:
The following, [(A)D&D](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons) inspired, [level structure](https://github.com/HubTou/PNU/discussions/2) is proposed for [gamification](https://en.wikipedia.org/wiki/Gamification).
We suggest level bosses in order to complete a level (but no [Demogorgon](https://en.wikipedia.org/wiki/Demogorgon#Dungeons_&_Dragons) here, we are not in [Stranger Things](https://en.wikipedia.org/wiki/Stranger_Things) :-)) and associated :trophy: trophies for fun :-)

We're also thinking about offering [Habitica](https://habitica.com/)'s quests for further gamification.

`The following classification of commands is still in progress.`

## Basic levels
### Level 1 sub projects
Handling return codes, printing to the terminal:
* [true](https://www.freebsd.org/cgi/man.cgi?query=true), [false](https://www.freebsd.org/cgi/man.cgi?query=false)
* [yes](https://www.freebsd.org/cgi/man.cgi?query=yes)
* [echo](https://www.freebsd.org/cgi/man.cgi?query=echo) => suggested level boss. Trophy: :baby_bottle: (hint: option can be [hardcoded](http://www.catb.org/jargon/html/H/hardcoded.html))

### Level 2 sub projects
Basic [string handling](https://docs.python.org/3/library/string.html):
* [basename, dirname](https://www.freebsd.org/cgi/man.cgi?query=basename) => without options for a start
* [caesar, rot13](https://www.freebsd.org/cgi/man.cgi?query=caesar)

Basic math or data structures, school level:
* [factor, primes](https://www.freebsd.org/cgi/man.cgi?query=factor) => suggested level boss. Trophy: :school_satchel:

### Level 3 sub projects
Basic [filters](https://github.com/HubTou/PNU/tree/main/_demos/gorgon), command line & [environment](https://www.freebsd.org/cgi/man.cgi?query=environ) processing, file operations:
* [basename](https://www.freebsd.org/cgi/man.cgi?query=basename) => with full options
* [cat](https://www.freebsd.org/cgi/man.cgi?query=cat) => POSIX version only for a start
* [head](https://www.freebsd.org/cgi/man.cgi?query=head)
* [expand, unexpand](https://www.freebsd.org/cgi/man.cgi?query=expand)
* [fold](https://www.freebsd.org/cgi/man.cgi?query=fold)
* [wc](https://www.freebsd.org/cgi/man.cgi?query=wc) => suggested level boss. Trophy: :toilet:

### Level 4 sub projects
Basic text processing utilities, multiple files or many options:
* [cat](https://www.freebsd.org/cgi/man.cgi?query=cat) => with full options
* [nl](https://www.freebsd.org/cgi/man.cgi?query=nl)
* [cmp](https://www.freebsd.org/cgi/man.cgi?query=cmp)
* [comm](https://www.freebsd.org/cgi/man.cgi?query=comm)
* [uniq](https://www.freebsd.org/cgi/man.cgi?query=uniq) => suggested level boss. Trophy: :one:

### Level 5 sub projects
Basic utilities using more complex parsing:
* [expr](https://www.freebsd.org/cgi/man.cgi?query=expr) => just a warmer
* [printf](https://www.freebsd.org/cgi/man.cgi?query=printf)
* [getopts](https://www.freebsd.org/cgi/man.cgi?query=getopts)
* [cut](https://www.freebsd.org/cgi/man.cgi?query=cut) => suggested level boss. Trophy: :scissors:

## Intermediate levels
System utilities (implying minimum Unix system knowledge).
[Regular expressions](https://docs.python.org/3/library/re.html), text parsing.
[CSV](https://docs.python.org/3/library/csv.html), [JSON](https://docs.python.org/3/library/json.html), [XML](https://docs.python.org/3/library/xml.html), [HTML](https://docs.python.org/3/library/html.html) data handling.

### Level 6 sub projects
Basic system utilities.

### Level 7 sub projects
Basic system utilities, possibly recursive ones:

### Level 8 sub projects
### Level 9 sub projects
### Level 10 sub projects

## Advanced levels
Full screen text applications, windowed applications, office documents manipulation, image manipulation, web scraping, network applications, automation.

Interactive full screen applications:
* [vi](https://www.freebsd.org/cgi/man.cgi?query=vi)

Advanced system utilities, data compression:
* [compress, uncompress](https://www.freebsd.org/cgi/man.cgi?query=compress)
* [zcat](https://www.freebsd.org/cgi/man.cgi?query=zcat)

### Level 11 sub projects
### Level 12 sub projects
### Level 13 sub projects
### Level 14 sub projects
### Level 15 sub projects

## Master levels
Languages (interpreters, compilers), database management systems, network protocols:

* [awk](https://www.freebsd.org/cgi/man.cgi?query=awk)

### Level 16 sub projects
### Level 17 sub projects
### Level 18 sub projects
### Level 19 sub projects
 
### Level 20 sub projects
* [sh](https://www.freebsd.org/cgi/man.cgi?query=sh) => Suggested level boss. Trophy: :shell:

## Immortal levels
It's a long way to the top if you wanna get your entry in the "Deities & [Demigods](http://www.catb.org/jargon/html/D/demigod.html)" of hackers, but here are some examples to inspire you from the [Unix & open source pantheon](https://www.facesofopensource.com/unix/) (note: having a :neckbeard: [beard](http://jargonf.org/wiki/barbu) is not mandatory)

However, all of this is beyond the scope of the project and probably not a good idea to implement in [Python](http://www.catb.org/jargon/html/P/Python.html) :-)

### Demigods level transcending projects
Full operating system kernels & device drivers:
* Your own [Minix](https://en.wikipedia.org/wiki/Minix)/[386BSD](https://en.wikipedia.org/wiki/386BSD)/[Linux](http://www.catb.org/jargon/html/L/Linux.html) like operating system with PNU [userland](http://www.catb.org/jargon/html/U/userland.html) utilities :-)

### Deities level transcending projects
Making your own hardware platform and all the software to run it.
* Although not Unix related, :mage_man: [The Woz](https://en.wikipedia.org/wiki/Steve_Wozniak) springs to mind here and his excellent autobiography, [iWoz](https://en.wikipedia.org/wiki/IWoz), is highly recommended for a good glimpse into a true [hacker](http://www.catb.org/jargon/html/H/hacker.html)'s mind.

