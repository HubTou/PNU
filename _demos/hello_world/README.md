# hello_world
This is [traditionally the first program a coder is supposed to write in a new environment](http://www.catb.org/~esr/jargon/html/H/hello-world.html).

Let's explain what is inside this overcomplicated version.

```Python
#!/usr/bin/env python3
```

* The first line of the script, when it starts with the [magic](http://www.catb.org/~esr/jargon/html/M/magic-number.html) string "#!", is called a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))
(from "[shell bang](http://www.catb.org/~esr/jargon/html/S/shebang.html)").
* Its purpose is to indicate the name of the software that will be used to interpret the rest of the file.
* You can directly use the path to your interpreter, for example "#!/bin/sh".
* But for Python it is recommended to use "#!/usr/bin/env python" instead for portability sake
(the "env" program will find the location of your Python interpreter in one of the directories indicated in the
[PATH](http://www.catb.org/~esr/jargon/html/P/path.html) environment variable.
* This will not be used in Windows operating systems, as they rely on file extensions to know which interpreter to use.

```Python
""" hello_world - say hello to the world
License: 3-clause BSD (see https://opensource.org/licenses/BSD-3-Clause)
Author: Hubert Tournier
"""
```

* The second line of a Python script starts a comment called a [docstring](https://www.python.org/dev/peps/pep-0008/#documentation-strings) (from "documentation
  string") and is specified in the [PEP 257 convention](https://www.python.org/dev/peps/pep-0257/).
* This peculiar docstring comments the whole program.
* You should put a one line description of your program on the first line of the comment.
* I use the same structure than what the [whatis](https://www.freebsd.org/cgi/man.cgi?query=whatis) command returns: the name of the program - the one line description.
* The rest of the comment contents are free.
* I usually mention at least:
  * the license used (you can [choose an open source one](https://opensource.org/licenses/) on the [Open Source Initiative](https://opensource.org/) (OSI) web site)
    * Personnally, I favor the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause) because I'm [open source](http://www.catb.org/~esr/jargon/html/O/open-source.html) / [copycenter](http://www.catb.org/~esr/jargon/html/C/copycenter.html) minded
    * Some others would favor the [GNU General Public License](https://opensource.org/licenses/gpl-license) (GPL) because they would be more [free software](http://www.catb.org/~esr/jargon/html/F/free-software.html) / [copyleft](http://www.catb.org/~esr/jargon/html/C/copyleft.html) oriented ([IMNSHO](http://www.catb.org/~esr/jargon/html/I/IMHO.html) we should say freed software rather than free) 
  * the author's name
  * I think it's best not to clutter the source code with explanations that you can put in accompanying [documentation](http://www.catb.org/~esr/jargon/html/D/documentation.html)...
* You should also add docstrings for all **public** modules, functions, classes and methods, immediately after the def line.

```Python
import sys
```

* The next part of the script is the import section.
* The [PEP8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) has some [recommandations for this section layout](https://www.python.org/dev/peps/pep-0008/#imports), but you should definitely check the Style Guide as a whole!
* The sys module will be needed for the exit() function that we will use at the end to close the program properly.
* It's possible to import only the module's contents into our namespace ("from sys import \*"), but I prefer to prefix external functions by their module name for the sake of clarity. 

```Python
# Version string used by the what(1) and ident(1) commands:
ID = "@(#) $Id: hello_world - say hello to the world v1.0.0 (May 13, 2021) by Hubert Tournier $"
```

```Python
print("Hello, world!")
```

```Python
sys.exit(0)
```

* the **last** line of our program provides
