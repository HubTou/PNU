
VERSION=1.0.0

echobox.1.gz: echobox.1
	gzip -k9 echobox.1

tarball:
	tar czf echobox-${VERSION}.tar.gz License Makefile echobox.*

install: echobox.1.gz
	install -m 0755 -o root -g wheel echobox.py /usr/local/bin/echobox
	install -m 0644 -o root -g wheel echobox.1.gz /usr/local/man/man1

uninstall:
	rm -f /usr/local/bin/echobox
	rm -f /usr/local/man/man1/echobox.1.gz

clean:
	rm -f echobox.1.gz

fullclean: clean
	rm -f echobox-${VERSION}.tar.gz
