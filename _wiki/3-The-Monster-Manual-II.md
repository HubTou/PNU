# [The Monster Manual II](https://en.wikipedia.org/wiki/Monster_Manual_II)
This page lists non-POSIX commands available in modern [FreeBSD](https://www.freebsd.org/), along with the short description provided by the [whatis](https://www.freebsd.org/cgi/man.cgi?query=whatis)(1) command, links to manual pages, [FreeBSD source code](https://github.com/freebsd/freebsd-src), number of Single Lines of Code (without comments), languages identified, and eventual [Jargon file](http://www.catb.org/jargon/html/index.html) or [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) entry..

We also made a selection of commands that would be interesting to reimplement, though it's by no means a limitation to your creativity :-)

## FreeBSD /bin commands
### FreeBSD /bin commands selected for reimplementation
Command|Whatis|man|src|SLOC|Languages|Other|Comments
---|---|---|---|---|---|---|---
domainname|set or print name of current YP/NIS domain|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=domainname&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/domainname)|40|C||
getfacl|get ACL information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=getfacl&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/getfacl)|229|C||
hostname|set or print name of current host system|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=hostname&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/hostname)|58|C||
realpath|return resolved physical path|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=realpath&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/realpath)|40|C||
setfacl|set ACL information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=setfacl&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/setfacl)|764|C||
uuidgen|generate universally unique identifiers|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=uuidgen&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/uuidgen)|76|C||

### Other FreeBSD /bin commands
Command|Whatis|man|src|SLOC|Languages|Other|Comments
---|---|---|---|---|---|---|---
chflags|change file flags|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=chflags&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/chflags)|173|C, Bash||Non portable
chio|medium changer control utility|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=chio&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/chio)|777|C||Non portable
csh|C shell with file name completion and command line editing|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=csh&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/csh)|147|C||Other shell
freebsd-version|freebsd-version(1) - print the version and patch level of the installed system|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=freebsd-version&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/freebsd-version)|0|||Non portable
kenv|dump or modify the kernel environment|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=kenv&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/kenv)|140|C||Non portable
pgrep|find or signal processes by name|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=pgrep&manpath=FreeBSD+13.0-current)|||||Multi process
pkill|find or signal processes by name|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=pkill&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/pkill)|1484|Bash, C||Multi process
pwait|wait for processes to terminate|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=pwait&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/pwait)|357|Bash, C||Multi process
red|text editor|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=red&manpath=FreeBSD+13.0-current)|||||Editor
rmail|handle remote mail received via uucp|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=rmail&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/rmail)|0|||UUCP
sync|force completion of pending disk writes (flush cache)|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=sync&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/sync)|14|C|[jargon](http://www.catb.org/jargon/html/S/sync.html)|System
tcsh|C shell with file name completion and command line editing|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=tcsh&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/contrib/tcsh)|40933|C, Tcsh, EmacsLisp||Other shell

## FreeBSD /usr/bin commands
### FreeBSD /usr/bin commands selected for reimplementation
Command|Whatis|man|src|SLOC|Languages|Other|Comments
---|---|---|---|---|---|---|---
apply|apply a command to a set of arguments|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=apply&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/apply)|156|C, Bash||
apropos|search manual page databases|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=apropos&manpath=FreeBSD+13.0-current)|||||
banner|print large banner on printer|[freebsd(6)](https://www.freebsd.org/cgi/man.cgi?query=banner&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/banner)|1086|C|[jargon](http://www.catb.org/jargon/html/B/banner.html)|
caesar|decrypt caesar ciphers|[freebsd(6)](https://www.freebsd.org/cgi/man.cgi?query=caesar&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/caesar)|77|C, Bash||
col|filter reverse line feeds from input|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=col&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/col)|484|C, Bash||
colrm|remove columns from a file|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=colrm&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/colrm)|84|C||
column|columnate lists|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=column&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/column)|242|C||
cpio|copy files to and from archives||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/cpio)|13|Bash||
dc|dc|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=dc&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/dc)|2124|C, Bash||
dialog|display dialog boxes from shell scripts|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=dialog&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/contrib/dialog)|16721|C, Perl, Python, Bash||
egrep|file pattern searcher|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=egrep&manpath=FreeBSD+13.0-current)|||||
factor|factor a number, generate primes|[freebsd(6)](https://www.freebsd.org/cgi/man.cgi?query=factor&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/factor)|240|C|[jargon](http://www.catb.org/jargon/html/F/factor.html)|
fetch|retrieve a file by Uniform Resource Locator|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=fetch&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/fetch)|837|C||
fgrep|file pattern searcher|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=fgrep&manpath=FreeBSD+13.0-current)|||||
fmt|simple text formatter|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=fmt&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/fmt)|386|C||
fortune|print a random, hopefully interesting, adage|[freebsd(6)](https://www.freebsd.org/cgi/man.cgi?query=fortune&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/fortune)|1329|C, Python||
getopt|parse command options|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=getopt&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/getopt)|31|C||
hd|ASCII, decimal, hexadecimal, octal dump|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=hd&manpath=FreeBSD+13.0-current)|||||
hexdump|ASCII, decimal, hexadecimal, octal dump||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/hexdump)|1418|C, Bash||
ident|identify RCS keyword string in files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ident&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ident)|169|C, Bash||
install|install binaries|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=install&manpath=FreeBSD+13.0-current)|||||
jot|print sequential or random data|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=jot&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/jot)|443|C, Bash||
less|opposite of more|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=less&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/less)|122|C, Bash||
locate|find filenames quickly|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=locate&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/locate)|859|C, Bash||
look|display lines beginning with a given string|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=look&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/look)|185|C||
makewhatis|index UNIX manuals|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=makewhatis&manpath=FreeBSD+13.0-current)|||||
manpath|display search path for manual pages|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=manpath&manpath=FreeBSD+13.0-current)|||||
morse|reformat input as morse code|[freebsd(6)](https://www.freebsd.org/cgi/man.cgi?query=morse&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/morse)|335|C||
nawk|pattern-directed scanning and processing language|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=nawk&manpath=FreeBSD+13.0-current)|||||
nc|arbitrary TCP and UDP connections and listens|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=nc&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/nc)|0|||
ncal|displays a calendar and the date of Easter|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ncal&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ncal)|803|C, Bash||
number|convert Arabic numerals to English|[freebsd(6)](https://www.freebsd.org/cgi/man.cgi?query=number&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/number)|176|C||
pom|display the phase of the moon|[freebsd(6)](https://www.freebsd.org/cgi/man.cgi?query=pom&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/pom)|153|C||
primes|factor a number, generate primes|[freebsd(6)](https://www.freebsd.org/cgi/man.cgi?query=primes&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/primes)|1160|C||
printenv|print out the environment|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=printenv&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/printenv)|48|C||
random|random lines from a file or random numbers|[freebsd(6)](https://www.freebsd.org/cgi/man.cgi?query=random&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/random)|296|C|[jargon](http://www.catb.org/jargon/html/R/random.html)|
rev|reverse lines of a file|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=rev&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/rev)|62|C||
rgrep|file pattern searcher|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=rgrep&manpath=FreeBSD+13.0-current)|||||
rot13|decrypt caesar ciphers|[freebsd(6)](https://www.freebsd.org/cgi/man.cgi?query=rot13&manpath=FreeBSD+13.0-current)||||[jargon](http://www.catb.org/jargon/html/R/rot13.html)|
script|make typescript of terminal session|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=script&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/script)|402|C||
sdiff|side-by-side diff|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=sdiff&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/sdiff)|898|C, Bash||
seq|print sequences of numbers|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=seq&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/seq)|318|C, Bash||
shar|create a shell archive of files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=shar&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/shar)|33|Bash||
strfile|create a random access file for storing strings|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=strfile&manpath=FreeBSD+13.0-current)|||||
sum|display file checksums and block counts|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=sum&manpath=FreeBSD+13.0-current)|||||
tar|manipulate tape archives||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/tar)|13|Bash||
timeout|run a command with a time limit|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=timeout&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/timeout)|391|C, Bash||
truncate|truncate or extend the length of files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=truncate&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/truncate)|359|Bash, C||
units|conversion calculator|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=units&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/units)|643|C, Bash||
whatis|search manual page databases|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=whatis&manpath=FreeBSD+13.0-current)|||||
whereis|locate programs|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=whereis&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/whereis)|457|C||
which|locate a program file in the user's path|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=which&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/which)|83|C||
xo|emit formatted output based on format string and arguments|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=xo&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/xo)|30|Bash||
yes|be repetitively affirmative|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=yes&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/yes)|40|C||

### Other FreeBSD /usr/bin commands
Command|Whatis|man|src|SLOC|Languages|Other|Comments
---|---|---|---|---|---|---|---
CC|||||||
Mail|||||||
addr2line|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/addr2line)|0|||
asn1_compile|||||||
atq|queue, examine or delete jobs for later execution|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=atq&manpath=FreeBSD+13.0-current)|||||
atrm|queue, examine or delete jobs for later execution|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=atrm&manpath=FreeBSD+13.0-current)|||||
b64decode|encode/decode a binary file|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=b64decode&manpath=FreeBSD+13.0-current)|||||
b64encode|encode/decode a binary file|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=b64encode&manpath=FreeBSD+13.0-current)|||||
backlight|configure backlight hardware|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=backlight&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/backlight)|163|C||
biff|be notified if mail arrives and who it is from|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=biff&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/biff)|60|C|[jargon](http://www.catb.org/jargon/html/B/biff.html)|
brandelf|mark an ELF binary for a specific ABI|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=brandelf&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/brandelf)|151|C||
bsdcat|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/bsdcat)|13|Bash||
bsdcpio|||||||
bsdiff|generate a patch between two binary files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=bsdiff&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/bsdiff)|505|C||
bsdtar|||||||
bsnmpget|simple tools for querying SNMP agents|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=bsnmpget&manpath=FreeBSD+13.0-current)|||||
bsnmpset|simple tools for querying SNMP agents|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=bsnmpset&manpath=FreeBSD+13.0-current)|||||
bsnmpwalk|simple tools for querying SNMP agents|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=bsnmpwalk&manpath=FreeBSD+13.0-current)|||||
bspatch|apply a patch built with bsdiff 1|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=bspatch&manpath=FreeBSD+13.0-current)|||||
bthost|look up Bluetooth host names and Protocol Service Multiplexor values|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=bthost&manpath=FreeBSD+13.0-current)|||||
btsockstat|show Bluetooth sockets information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=btsockstat&manpath=FreeBSD+13.0-current)|||||
bunzip2|a block-sorting file compressor, v1.0.8 bzcat - decompresses files to stdout bzip2recover - recovers data from damaged bzip2 files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=bunzip2&manpath=FreeBSD+13.0-current)|||||
byacc|an LALR(1) parser generator|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=byacc&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/contrib/byacc)|84795|C, Bash||
bzcat|a block-sorting file compressor, v1.0.8 bzcat - decompresses files to stdout bzip2recover - recovers data from damaged bzip2 files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=bzcat&manpath=FreeBSD+13.0-current)|||||
bzegrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=bzegrep&manpath=FreeBSD+13.0-current)|||||
bzfgrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=bzfgrep&manpath=FreeBSD+13.0-current)|||||
bzgrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=bzgrep&manpath=FreeBSD+13.0-current)|||||
bzip2|a block-sorting file compressor, v1.0.8 bzcat - decompresses files to stdout bzip2recover - recovers data from damaged bzip2 files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=bzip2&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/bzip2)|0|||
bzip2recover|a block-sorting file compressor, v1.0.8 bzcat - decompresses files to stdout bzip2recover - recovers data from damaged bzip2 files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=bzip2recover&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/bzip2recover)|0|||
bzless|||||||
c++|||||||
c++filt|||||||
c89|POSIX.2 C language compiler|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=c89&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/c89)|46|C||
calendar|reminder service|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=calendar&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/calendar)|2667|C, Bash||
cap_mkdb|create capability database|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=cap_mkdb&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/cap_mkdb)|149|C||
cc|||||||
chat|Automated conversational script with a modem|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=chat&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/chat)|978|C||
chfn|add or change user database information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=chfn&manpath=FreeBSD+13.0-current)|||||
chkey|change your encryption key|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=chkey&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/chkey)|177|C||
chpass|add or change user database information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=chpass&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/chpass)|704|C||
chsh|add or change user database information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=chsh&manpath=FreeBSD+13.0-current)|||||
clang|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/clang)|1|Bash||
clang++|||||||
clang-cpp|clang, c++, cc, CC, clang++, clang-cpp, cpp(1) - the Clang C, C++, and Objective-C compiler|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=clang-cpp&manpath=FreeBSD+13.0-current)|||||
clang-tblgen|||||||
clear|terminal capability interface||||||
compile_et|error table compiler|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=compile_et&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/compile_et)|0|||
cpp|clang, c++, cc, CC, clang++, clang-cpp, cpp(1) - the Clang C, C++, and Objective-C compiler|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=cpp&manpath=FreeBSD+13.0-current)|||||
cpuset|configure processor sets|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=cpuset&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/cpuset)|332|C||
crunchgen|generates build environment for a crunched binary|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=crunchgen&manpath=FreeBSD+13.0-current)|||||
crunchide|hides symbol names from ld, for crunching programs together|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=crunchide&manpath=FreeBSD+13.0-current)|||||
crypt|||||||
ctfconvert|convert debug data to CTF data|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ctfconvert&manpath=FreeBSD+13.0-current)|||||
ctfdump|dump the SUNW_ctf section of an ELF file|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ctfdump&manpath=FreeBSD+13.0-current)|||||
ctfmerge|merge several CTF data sections into one|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ctfmerge&manpath=FreeBSD+13.0-current)|||||
ctlstat|CAM Target Layer statistics utility|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=ctlstat&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ctlstat)|555|C||
cu|call UNIX|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=cu&manpath=FreeBSD+13.0-current)|||||
diff3|compare three files line by line|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=diff3&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/diff3)|520|C, Bash||
dpv|stream data from stdin or multiple paths with dialog progress view|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=dpv&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/dpv)|365|C||
drill|get (debug) information out of DNS(SEC)|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=drill&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/drill)|0|||
dtc|device tree compiler|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=dtc&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/dtc)|3221|C++||
edit|easy editor|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=edit&manpath=FreeBSD+13.0-current)|||||
ee|easy editor|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ee&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ee)|0|||
elfctl|change an ELF binary's feature control note|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=elfctl&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/elfctl)|288|C||
elfdump|display information about ELF files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=elfdump&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/elfdump)|989|C||
enigma|very simple file encryption|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=enigma&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/enigma)|112|C||
etdump|Dump El Torito boot catalog information from ISO images|[freebsd(1, 8)](https://www.freebsd.org/cgi/man.cgi?query=etdump&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/etdump)|261|C||
file2c|convert file to c-source|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=file2c&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/file2c)|79|C, Bash||
finger|user information lookup program|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=finger&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/finger)|1066|C|[jargon](http://www.catb.org/jargon/html/F/finger.html)|
flex|fast lexical analyzer generator|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=flex&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/contrib/flex)|6254|C, Bash||
flex++|||||||
from|print names of those who have sent mail|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=from&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/from)|106|C||
fstat|identify active files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=fstat&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/fstat)|740|C||
fsync|synchronize a file's in-core state with that on disk|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=fsync&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/fsync)|35|C||
ftp|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ftp)|135|C||
gate-ftp|ftp, gate-ftp, pftp(1) - Internet file transfer program|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=gate-ftp&manpath=FreeBSD+13.0-current)|||||
gcore|get core images of running process|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=gcore&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/gcore)|857|C||
gcov|llvm-cov, gcov(1) - emit coverage information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=gcov&manpath=FreeBSD+13.0-current)|||||
getaddrinfo|resolve names to socket addresses|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=getaddrinfo&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/getaddrinfo)|228|C, Awk||
getent|get entries from administrative database|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=getent&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/getent)|489|C||
gprof|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/gprof)|2017|C||
grdc|grand digital clock (curses)|[freebsd(6)](https://www.freebsd.org/cgi/man.cgi?query=grdc&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/grdc)|185|C||
groups|show group memberships|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=groups&manpath=FreeBSD+13.0-current)|||||
gunzip|compression/decompression tool using Lempel-Ziv coding (LZ77)|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=gunzip&manpath=FreeBSD+13.0-current)|||||
gzcat|compression/decompression tool using Lempel-Ziv coding (LZ77)|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=gzcat&manpath=FreeBSD+13.0-current)|||||
gzexe|create auto-decompressing executables|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=gzexe&manpath=FreeBSD+13.0-current)|||||
gzip|compression/decompression tool using Lempel-Ziv coding (LZ77)|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=gzip&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/gzip)|2753|C||
host|DNS lookup utility||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/host)|0|||
hxtool|||||||
ibstat|open InfiniBand diagnostics||||||
ibv_asyncwatch|display asynchronous events|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ibv_asyncwatch&manpath=FreeBSD+13.0-current)|||||
ibv_devices|list RDMA devices|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ibv_devices&manpath=FreeBSD+13.0-current)|||||
ibv_devinfo|query RDMA devices|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ibv_devinfo&manpath=FreeBSD+13.0-current)|||||
ibv_rc_pingpong|simple InfiniBand RC transport test|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ibv_rc_pingpong&manpath=FreeBSD+13.0-current)|||||
ibv_srq_pingpong|simple InfiniBand shared receive queue test|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ibv_srq_pingpong&manpath=FreeBSD+13.0-current)|||||
ibv_uc_pingpong|simple InfiniBand UC transport test|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ibv_uc_pingpong&manpath=FreeBSD+13.0-current)|||||
ibv_ud_pingpong|simple InfiniBand UD transport test|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ibv_ud_pingpong&manpath=FreeBSD+13.0-current)|||||
indent|indent and format C program source|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=indent&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/indent)|2464|C, Bash, Prolog||
iscsictl|iSCSI initiator management utility|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=iscsictl&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/iscsictl)|960|C||
kadmin|Kerberos administration utility|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=kadmin&manpath=FreeBSD+13.0-current)|||||
kcc|||||||
kdestroy|remove one credential or destroy the current ticket file|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=kdestroy&manpath=FreeBSD+13.0-current)|||||
kdump|display kernel trace data|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=kdump&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/kdump)|1855|C||
keylogin|decrypt and store secret key|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=keylogin&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/keylogin)|35|C||
keylogout|delete stored secret key|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=keylogout&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/keylogout)|20|C||
kf|securely forward tickets|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=kf&manpath=FreeBSD+13.0-current)|||||
kgetcred|get a ticket for a particular service|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=kgetcred&manpath=FreeBSD+13.0-current)|||||
killall|kill processes by name|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=killall&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/killall)|347|C||
kinit|acquire initial tickets|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=kinit&manpath=FreeBSD+13.0-current)|||||
klist|list Kerberos credentials|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=klist&manpath=FreeBSD+13.0-current)|||||
kpasswd|Kerberos 5 password changing program|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=kpasswd&manpath=FreeBSD+13.0-current)|||||
krb5-config|krb5-config(1) - give information on how to link code against Heimdal libraries|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=krb5-config&manpath=FreeBSD+13.0-current)|||||
ksu|||||||
kswitch|switch between default credential caches|[freebsd(1, SECTION)](https://www.freebsd.org/cgi/man.cgi?query=kswitch&manpath=FreeBSD+13.0-current)|||||
ktrace|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ktrace)|235|C||
ktrdump|print kernel ktr trace buffer|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=ktrdump&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ktrdump)|286|C||
kyua|Testing framework for infrastructure software|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=kyua&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/kyua)|0|||
lam|laminate files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lam&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/lam)|165|C||
last|indicate last logins of users and ttys|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=last&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/last)|415|C||
lastcomm|show last commands executed|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lastcomm&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/lastcomm)|379|C, Bash||
ld|The GNU linker|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ld&manpath=FreeBSD+13.0-current)|||||
ld.lld|ELF linker from the LLVM project|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ld.lld&manpath=FreeBSD+13.0-current)|||||
ldd|list dynamic object dependencies|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ldd&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ldd)|327|C||
ldd32|list dynamic object dependencies|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ldd32&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ldd32)|0|||
leave|remind you when you have to leave|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=leave&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/leave)|113|C||
lessecho|expand metacharacters|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lessecho&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/lessecho)|0|||
lesskey|specify key bindings for less|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lesskey&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/lesskey)|0|||
lesspipe.sh|||||||
lex++|||||||
limits|set or display process resource limits|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=limits&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/limits)|574|C, Bash||
lldb|LLDB Documentation|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lldb&manpath=FreeBSD+13.0-current)|||||
lldb-tblgen|||||||
llvm-addr2line|llvm-addr2line(1) - a drop-in replacement for addr2line|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=llvm-addr2line&manpath=FreeBSD+13.0-current)|||||
llvm-ar|llvm-ar(1) - LLVM archiver|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=llvm-ar&manpath=FreeBSD+13.0-current)|||||
llvm-cov|||||||
llvm-cxxfilt|||||||
llvm-nm|llvm-nm(1) - list LLVM bitcode and object file's symbol table|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=llvm-nm&manpath=FreeBSD+13.0-current)|||||
llvm-objdump|llvm-objdump(1) - LLVM object file dumper|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=llvm-objdump&manpath=FreeBSD+13.0-current)|||||
llvm-profdata|llvm-profdata(1) - Profile data tool|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=llvm-profdata&manpath=FreeBSD+13.0-current)|||||
llvm-ranlib|llvm-ranlib(1) - generates an archive index|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=llvm-ranlib&manpath=FreeBSD+13.0-current)|||||
llvm-symbolizer|llvm-symbolizer(1) - convert addresses into source code locations|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=llvm-symbolizer&manpath=FreeBSD+13.0-current)|||||
llvm-tblgen|llvm-tblgen, tblgen(1) - Target Description To C++ Code Generator|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=llvm-tblgen&manpath=FreeBSD+13.0-current)|||||
lock|reserve a terminal|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lock&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/lock)|205|C||
lockf|execute a command while holding a file lock|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lockf&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/lockf)|129|C||
login|log into the computer|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=login&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/login)|780|C||
logins|display account information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=logins&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/logins)|278|C||
lorder|list dependencies for object files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lorder&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/lorder)|30|Bash||
lpq|||||||
lpr|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.sbin/lpr)|8839|C, Bash||
lprm|||||||
lsvfs|list installed virtual file systems|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lsvfs&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/lsvfs)|68|C||
lzcat|Compress or decompress .xz and .lzma files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lzcat&manpath=FreeBSD+13.0-current)|||||
lzdec|||||||
lzegrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lzegrep&manpath=FreeBSD+13.0-current)|||||
lzfgrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lzfgrep&manpath=FreeBSD+13.0-current)|||||
lzgrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lzgrep&manpath=FreeBSD+13.0-current)|||||
lzless|||||||
lzma|Compress or decompress .xz and .lzma files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lzma&manpath=FreeBSD+13.0-current)|||||
lzmainfo|show information stored in the .lzma file header|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=lzmainfo&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/lzmainfo)|0|||
mail|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/mail)|5672|C||
mailq|print the mail queue|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=mailq&manpath=FreeBSD+13.0-current)|||||
make-roken|||||||
mandoc|format manual pages|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=mandoc&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/mandoc)|0|||
mckey|RDMA CM multicast setup and simple data transfer test.|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=mckey&manpath=FreeBSD+13.0-current)|||||
minigzip|minimal implementation of the 'gzip' compression tool|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=minigzip&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/minigzip)|0|||
ministat|statistics utility|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ministat&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ministat)|535|C||
mkcsmapper|generates hashed conversion data for iconv 3|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=mkcsmapper&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/mkcsmapper)|10|C||
mkdep|construct Makefile dependency list|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=mkdep&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/mkdep)|88|Bash||
mkesdb|generates conversion catalog for iconv 3|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=mkesdb&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/mkesdb)|8|C||
mkimg|utility to make disk images|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=mkimg&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/mkimg)|3249|C, Bash||
mkstr|create an error message file by massaging C source|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=mkstr&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/mkstr)|210|C||
mktemp|make temporary file name (unique)|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=mktemp&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/mktemp)|87|C||
mkuzip|compress disk image for use with geom_uzip 4 class|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=mkuzip&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/mkuzip)|967|C||
msgs|system messages and junk mail program|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=msgs&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/msgs)|611|C||
mt|magnetic tape manipulating program|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=mt&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/mt)|1138|C||
netstat|show network status and statistics|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=netstat&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/netstat)|6065|C||
newaliases|rebuild the data base for the mail aliases file|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=newaliases&manpath=FreeBSD+13.0-current)|||||
newkey|create a new key in the publickey database|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=newkey&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/newkey)|432|C||
nex|text editors|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=nex&manpath=FreeBSD+13.0-current)|||||
nfsstat|display NFS statistics|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=nfsstat&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/nfsstat)|835|C||
ntpq|standard NTP query program|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=ntpq&manpath=FreeBSD+13.0-current)|||||
nvi|text editors|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=nvi&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/contrib/nvi)|26920|C, Awk||
nview|text editors|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=nview&manpath=FreeBSD+13.0-current)|||||
objcopy|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/objcopy)|0|||
openssl|||||||
opieinfo|Extract sequence number and seed for future OPIE challenges.|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=opieinfo&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/opieinfo)|0|||
opiekey|opiekey, otp-md4, otp-md5, otp-sha1(1) - Programs for computing responses to OTP challenges.|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=opiekey&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/opiekey)|0|||
opiepasswd|Change or set a user's password for the OPIE authentication system.|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=opiepasswd&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/opiepasswd)|0|||
otp-md4|opiekey, otp-md4, otp-md5, otp-sha1(1) - Programs for computing responses to OTP challenges.|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=otp-md4&manpath=FreeBSD+13.0-current)|||||
otp-md5|opiekey, otp-md4, otp-md5, otp-sha1(1) - Programs for computing responses to OTP challenges.|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=otp-md5&manpath=FreeBSD+13.0-current)|||||
otp-sha1|opiekey, otp-md4, otp-md5, otp-sha1(1) - Programs for computing responses to OTP challenges.|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=otp-sha1&manpath=FreeBSD+13.0-current)|||||
pagesize|print system page size|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=pagesize&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/pagesize)|2|Bash||
pargs|get detailed process information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=pargs&manpath=FreeBSD+13.0-current)|||||
passwd|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/passwd)|96|C||
penv|get detailed process information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=penv&manpath=FreeBSD+13.0-current)|||||
perror|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/perror)|29|C||
pftp|ftp, gate-ftp, pftp(1) - Internet file transfer program|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=pftp&manpath=FreeBSD+13.0-current)|||||
pgrep|find or signal processes by name|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=pgrep&manpath=FreeBSD+13.0-current)|||||
pkill|find or signal processes by name|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=pkill&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/bin/pkill)|1484|Bash, C||
pmcstudy|Perform various studies on a system's overall PMCs|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=pmcstudy&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.sbin/pmcstudy)|2587|C||
posixshmcontrol|Control POSIX shared memory segments|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=posixshmcontrol&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/posixshmcontrol)|401|C||
proccontrol|Control some process execution aspects|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=proccontrol&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/proccontrol)|301|C||
procstat|get detailed process information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=procstat&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/procstat)|2284|C, Bash||
protect|protect processes from being killed when swap space is exhausted|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=protect&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/protect)|75|C||
pwdx|get detailed process information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=pwdx&manpath=FreeBSD+13.0-current)|||||
quota|display disk usage and limits|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=quota&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/quota)|485|C||
ranlib|generate an index to an archive|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ranlib&manpath=FreeBSD+13.0-current)|||||
rctl|display and update resource limits database|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=rctl&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/rctl)|452|C||
readelf|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/readelf)|0|||
readlink|||||||
ree|easy editor|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ree&manpath=FreeBSD+13.0-current)|||||
reset|terminal initialization|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=reset&manpath=FreeBSD+13.0-current)|||||
resizewin|update terminal size|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=resizewin&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/resizewin)|88|C||
revoke|revoke a character device|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=revoke&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/revoke)|20|C||
rfcomm_sppd|RFCOMM Serial Port Profile daemon|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=rfcomm_sppd&manpath=FreeBSD+13.0-current)|||||
rpcgen|an RPC protocol compiler|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=rpcgen&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/rpcgen)|4076|C||
rpcinfo|report RPC information|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=rpcinfo&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/rpcinfo)|1222|C||
rping|RDMA CM connection and RDMA ping-pong test.|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=rping&manpath=FreeBSD+13.0-current)|||||
rs|reshape a data array|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=rs&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/rs)|535|C, Bash||
rup|remote status display|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=rup&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/rup)|150|C||
ruptime|show host status of local machines|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ruptime&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ruptime)|223|C||
rusers|who is logged in to machines on local network|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=rusers&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/rusers)|164|C||
rwall|send a message to users logged on a host|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=rwall&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/rwall)|91|C||
rwho|who is logged in on local machines|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=rwho&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/rwho)|168|C||
scp|secure copy (remote file copy program)|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=scp&manpath=FreeBSD+13.0-current)|||||
sftp|secure file transfer program|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=sftp&manpath=FreeBSD+13.0-current)|||||
showmount|show remote nfs mounts on host|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=showmount&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/showmount)|292|C||
size|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/size)|0|||
slc|||||||
slogin|OpenSSH SSH client (remote login program)|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=slogin&manpath=FreeBSD+13.0-current)|||||
smbutil|interface to the SMB requester|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=smbutil&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/smbutil)|0|||
sockstat|list open sockets|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=sockstat&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/sockstat)|1148|C||
soelim|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/soelim)|165|C, Bash||
sscop|SSCOP transport protocol|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=sscop&manpath=FreeBSD+13.0-current)|||||
ssh|||||||
ssh-add|ssh-add(1) - adds private key identities to the authentication agent|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ssh-add&manpath=FreeBSD+13.0-current)|||||
ssh-agent|ssh-agent(1) - authentication agent|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ssh-agent&manpath=FreeBSD+13.0-current)|||||
ssh-copy-id|ssh-copy-id(1) - copy public keys to a remote host|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ssh-copy-id&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ssh-copy-id)|56|Bash||
ssh-keygen|ssh-keygen(1) - authentication key generation, management and conversion|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ssh-keygen&manpath=FreeBSD+13.0-current)|||||
ssh-keyscan|ssh-keyscan(1) - gather SSH public keys|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ssh-keyscan&manpath=FreeBSD+13.0-current)|||||
stat|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/stat)|963|C, Bash||
stdbuf|change standard streams initial buffering|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=stdbuf&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/stdbuf)|64|C||
string2key|map a password into a key|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=string2key&manpath=FreeBSD+13.0-current)|||||
su|substitute user identity|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=su&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/su)|426|C||
svnlite|Subversion command line client tool|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=svnlite&manpath=FreeBSD+13.0-current)|||||
svnliteadmin|||||||
svnlitebench|||||||
svnlitedumpfilter|||||||
svnlitefsfs|||||||
svnlitelook|||||||
svnlitemucc|||||||
svnliterdump|||||||
svnliteserve|||||||
svnlitesync|||||||
svnliteversion|||||||
systat|display system statistics|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=systat&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/systat)|4795|C||
tcopy|copy and/or verify mag tapes|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=tcopy&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/tcopy)|233|C||
telnet|user interface to the TELNET protocol|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=telnet&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/telnet)|0|||
tftp|trivial file transfer program|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=tftp&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/tftp)|878|C||
tip|connect to a remote system|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=tip&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/tip)|3889|C||
top|display and update information about the top cpu processes|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=top&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/top)|3224|C||
truss|trace system calls|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=truss&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/truss)|3263|C||
tset|terminal initialization|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=tset&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/tset)|738|C||
ucmatose|RDMA CM connection and simple ping-pong test.|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ucmatose&manpath=FreeBSD+13.0-current)|||||
udaddy|RDMA CM datagram setup and simple ping-pong test.|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=udaddy&manpath=FreeBSD+13.0-current)|||||
ul|do underlining|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ul&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ul)|424|C||
unifdef|remove preprocessor conditionals from code|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=unifdef&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/unifdef)|1145|C, Bash||
unifdefall|remove preprocessor conditionals from code|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=unifdefall&manpath=FreeBSD+13.0-current)|||||
unlzma|Compress or decompress .xz and .lzma files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=unlzma&manpath=FreeBSD+13.0-current)|||||
unstr|create a random access file for storing strings|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=unstr&manpath=FreeBSD+13.0-current)|||||
unvis|revert a visual representation of data back to original form|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=unvis&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/unvis)|0|||
unxz|Compress or decompress .xz and .lzma files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=unxz&manpath=FreeBSD+13.0-current)|||||
unzip|extract files from a ZIP archive|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=unzip&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/unzip)|637|C||
unzstd|||||||
uptime|show how long system has been running|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=uptime&manpath=FreeBSD+13.0-current)||||[jargon](http://www.catb.org/jargon/html/U/uptime.html)|
usbhidaction|perform actions according to USB HID controls|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=usbhidaction&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/usbhidaction)|386|C||
usbhidctl|manipulate USB HID devices|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=usbhidctl&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/usbhidctl)|412|C||
users|list current users|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=users&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/users)|32|C++||
vacation|E-mail auto-responder|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=vacation&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/vacation)|0|||
verify_krb5_conf|checks krb5.conf for obvious errors|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=verify_krb5_conf&manpath=FreeBSD+13.0-current)|||||
view|text editors|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=view&manpath=FreeBSD+13.0-current)|||||
vis|display non-printable characters in a visual format|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=vis&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/vis)|0|||
vmstat|report virtual memory statistics|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=vmstat&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/vmstat)|1309|C||
vtfontcvt|convert font files for use by the video console|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=vtfontcvt&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/vtfontcvt)|800|C||
w|display who is logged in and what they are doing|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=w&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/w)|519|C||
wall|write a message to users|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=wall&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/wall)|295|C|[jargon](http://www.catb.org/jargon/html/W/wall.html)|
whoami|display effective user id|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=whoami&manpath=FreeBSD+13.0-current)|||||
whois|Internet domain name and network number directory service|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=whois&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/whois)|419|C||
xstr|extract strings from C programs to implement shared strings|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=xstr&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/xstr)|343|C||
xz|Compress or decompress .xz and .lzma files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=xz&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/xz)|0|||
xzcat|Compress or decompress .xz and .lzma files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=xzcat&manpath=FreeBSD+13.0-current)|||||
xzdec|Small .xz and .lzma decompressors|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=xzdec&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/xzdec)|0|||
xzdiff|compare compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=xzdiff&manpath=FreeBSD+13.0-current)|||||
xzegrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=xzegrep&manpath=FreeBSD+13.0-current)|||||
xzfgrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=xzfgrep&manpath=FreeBSD+13.0-current)|||||
xzgrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=xzgrep&manpath=FreeBSD+13.0-current)|||||
xzless|||||||
ypcat|print the values of all keys in a NIS database|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ypcat&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ypcat)|78|C||
ypchfn|add or change user database information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ypchfn&manpath=FreeBSD+13.0-current)|||||
ypchpass|add or change user database information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ypchpass&manpath=FreeBSD+13.0-current)|||||
ypchsh|add or change user database information|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ypchsh&manpath=FreeBSD+13.0-current)|||||
ypmatch|print the values of one or more keys in a NIS database|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ypmatch&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ypmatch)|77|C||
yppasswd|modify a user's password|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=yppasswd&manpath=FreeBSD+13.0-current)|||||
ypwhich|return hostname of NIS server of map master|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ypwhich&manpath=FreeBSD+13.0-current)|[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/ypwhich)|182|C||
zcmp|compare compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=zcmp&manpath=FreeBSD+13.0-current)|||||
zdiff|compare compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=zdiff&manpath=FreeBSD+13.0-current)|||||
zegrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=zegrep&manpath=FreeBSD+13.0-current)|||||
zfgrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=zfgrep&manpath=FreeBSD+13.0-current)|||||
zforce|force gzip files to have a .gz suffix|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=zforce&manpath=FreeBSD+13.0-current)|||||
zgrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=zgrep&manpath=FreeBSD+13.0-current)|||||
zinject|ZFS Fault Injector|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=zinject&manpath=FreeBSD+13.0-current)|||||
zless|view compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=zless&manpath=FreeBSD+13.0-current)|||||
zmore|view compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=zmore&manpath=FreeBSD+13.0-current)|||||
znew|convert compressed files to gzipped files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=znew&manpath=FreeBSD+13.0-current)|||||
zstd|||[src](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/zstd)|0|||
zstdcat|||||||
zstdegrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=zstdegrep&manpath=FreeBSD+13.0-current)|||||
zstdfgrep|grep compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=zstdfgrep&manpath=FreeBSD+13.0-current)|||||
zstdgrep|print lines matching a pattern in zstandard-compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=zstdgrep&manpath=FreeBSD+13.0-current)|||||
zstdless|view zstandard-compressed files|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=zstdless&manpath=FreeBSD+13.0-current)|||||
zstdmt|||||||
zstream|manipulate zfs send streams|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=zstream&manpath=FreeBSD+13.0-current)|||||
zstreamdump|filter data in zfs send stream|[freebsd(8)](https://www.freebsd.org/cgi/man.cgi?query=zstreamdump&manpath=FreeBSD+13.0-current)|||||
ztest|was written by the ZFS Developers as a ZFS unit test.|[freebsd(1)](https://www.freebsd.org/cgi/man.cgi?query=ztest&manpath=FreeBSD+13.0-current)|||||

