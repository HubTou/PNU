
VERSION=1.0.0
DESTROOTDIR=/usr/local

# Default action is to show this help message:
.help:
        @echo "Possible targets:"
        @echo "  tarball    Make a tar.gz file for distribution"
        @echo "  all        Make everything"
        @echo "  install    Install command and man page under ${DESTROOTDIR}"
        @echo "  uninstall  Uninstall command and man page from ${DESTROOTDIR}"
        @echo "  clean      Remove the compressed man page"
        @echo "  distclean  Remove everything made"

tarball:
        tar czf echobox-${VERSION}.tar.gz License Makefile README.md echobox.py echobox.1

echobox.1.gz: echobox.1
        @gzip -k9 echobox.1

all: tarball echobox.1.gz

install: echobox.1.gz
        install -m 0755 -o root -g wheel echobox.py ${DESTROOTDIR}/bin/echobox
        install -m 0644 -o root -g wheel echobox.1.gz ${DESTROOTDIR}/man/man1
        makewhatis

uninstall:
        rm -f ${DESTROOTDIR}/bin/echobox
        rm -f ${DESTROOTDIR}/man/man1/echobox.1.gz
        makewhatis

clean:
        @rm -f echobox.1.gz

distclean: clean
        @rm -f echobox-${VERSION}.tar.gz
