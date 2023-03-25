NAME=COMMAND
# Add your other source files on the following line:
SOURCES=src/${NAME}/__init__.py src/${NAME}/main.py # src/${NAME}/library.py

# Default action is to show this help message:
.help:
	@echo "Possible targets:"
	@echo "  check-code     Verify PEP 8 compliance (lint)"
	@echo "  check-security Verify security issues (audit)"
	@echo "  check-unused   Find unused code"
	@echo "  check-version  Find required Python version"
	@echo "  check-sloc     Count Single Lines of Code"
	@echo "  checks         Make all the previous tests"
	@echo "  format         Format code"
	@echo "  package        Build package"
	@echo "  upload-test    Upload the package to TestPyPi"
	@echo "  upload         Upload the package to PyPi"
	@echo "  distclean      Remove all generated files"

check-code: /usr/local/bin/pylint
	-pylint ${SOURCES}

lint: check-code

check-security: /usr/local/bin/bandit
	-bandit -r ${SOURCES}

audit: check-security

check-unused: /usr/local/bin/vulture
	-vulture --sort-by-size ${SOURCES}

check-version: /usr/local/bin/vermin
	-vermin ${SOURCES}

check-sloc: /usr/local/bin/pygount
	-pygount --format=summary .

checks: check-code check-security check-unused check-version check-sloc

format: /usr/local/bin/black
	black ${SOURCES}

love:
	@echo "Not war!"

man/${NAME}.1.gz: man/${NAME}.1
	@gzip -k9c man/${NAME}.1 > man/${NAME}.1.gz

# Uncomment the next comment if you offer a library interface

#man/${NAME}.3.gz: man/${NAME}.3
#	@gzip -k9c man/${NAME}.3 > man/${NAME}.3.gz

# Uncomment the commented parts in the next targets
# if you have an internationalized application:

#src/${NAME}/po/en/${NAME}.mo:
#	@msgfmt --output-file=src/${NAME}/po/en/${NAME}.mo src/${NAME}/po/en/${NAME}.po

#src/${NAME}/po/fr/${NAME}.mo:
#	@msgfmt --output-file=src/${NAME}/po/fr/${NAME}.mo src/${NAME}/po/fr/${NAME}.po

package: man/${NAME}.1.gz # man/${NAME}.3.gz src/${NAME}/po/en/${NAME}.mo src/${NAME}/po/fr/${NAME}.mo
	python -m build

upload-test:
	python -m twine upload --repository testpypi dist/*

upload:
	python -m twine upload dist/*

distclean:
	rm -rf build dist src/*.egg-info man/${NAME}.1.gz # man/${NAME}.3.gz src/${NAME}/po/en/${NAME}.mo src/${NAME}/po/fr/${NAME}.mo

