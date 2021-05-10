NAME=about
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
	tar czf ${NAME}-${VERSION}.tar.gz License Makefile README.md ${NAME}.py ${NAME}.1

${NAME}.1.gz: ${NAME}.1
	@gzip -k9 ${NAME}.1

all: tarball ${NAME}.1.gz

install: ${NAME}.1.gz
	install -m 0755 -o root -g wheel ${NAME}.py ${DESTROOTDIR}/bin/${NAME}
	install -m 0644 -o root -g wheel ${NAME}.1.gz ${DESTROOTDIR}/man/man1
	makewhatis

uninstall:
	rm -f ${DESTROOTDIR}/bin/${NAME}
	rm -f ${DESTROOTDIR}/man/man1/${NAME}.1.gz
	makewhatis

clean:
	@rm -f ${NAME}.1.gz

distclean: clean
	@rm -f ${NAME}-${VERSION}.tar.gz
