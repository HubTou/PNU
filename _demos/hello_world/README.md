# hello_world
This is [traditionally the first program a coder is supposed to write in a new environment](http://www.catb.org/~esr/jargon/html/H/hello-world.html).

Let's explain what is inside this overcomplicated version.

## Code commentary:
```Python
#!/usr/bin/env python3
```

* The first line of the script, when it starts with the [magic](http://www.catb.org/~esr/jargon/html/M/magic-number.html) string "#!", is called a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))
(from "[shell bang](http://www.catb.org/~esr/jargon/html/S/shebang.html)").
* Its purpose is to indicate the name of the software that will be used to interpret the rest of the file.
* You can directly use the path to your interpreter, for example "#!/bin/sh" for the [Bourne](https://en.wikipedia.org/wiki/Stephen_R._Bourne) [shell](http://www.catb.org/~esr/jargon/html/S/shell.html).
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
* The [sys module](https://docs.python.org/3/library/sys.html) will be needed for the exit() function that we will use at the end to close the program properly.
* It's possible to import the module's contents into our namespace ("from sys import \*"), but I prefer to prefix external functions by their module name for the sake of clarity. 

```Python
# Version string used by the what(1) and ident(1) commands:
ID = "@(#) $Id: hello_world - say hello to the world v1.0.0 (May 13, 2021) by Hubert Tournier $"
```

* Although unnecessary (and in fact unused by the program itself), the ID [constant](https://www.python.org/dev/peps/pep-0008/#constants) mention is a good practice to allow external programs to extract some information about your program (they also work with compiled software).
  * The [what](https://www.freebsd.org/cgi/man.cgi?query=what) command works with the original [SCCS version control system](https://en.wikipedia.org/wiki/Source_Code_Control_System) and searches for the magic string "@(#)":
  * The [ident](https://www.freebsd.org/cgi/man.cgi?query=ident) command works with the [RCS version control system](https://en.wikipedia.org/wiki/Revision_Control_System) and searches for the magic string "Id: ... $".
  * The number in braces behind the command names (ie. "what(1)") are a reference to the [section of the Unix manual](https://www.freebsd.org/cgi/man.cgi?query=man) describing them. 
* The combined form used above allows for a single declaration to fit both commands :-)
* Although [these 2 version control systems are deprecated](https://initialcommit.com/blog/Technical-Guide-VCS-Internals), their identification commands are still (sometimes) used in modern Unix systems.
* The [Pythonic way](https://www.python.org/dev/peps/pep-0020/) to do this would be to use the __version__ and __author__ [module level dunder variables](https://www.python.org/dev/peps/pep-0008/#module-level-dunder-names), however just putting the ID content into __version__ is not the correct way to use that variable according to the [PEP 440 Version Identification and Dependency Specification](https://www.python.org/dev/peps/pep-0440/).

```Python
print("Hello, world!")
```

* This could have been the only line in the script, but it would have felt so lonely!

```Python
sys.exit(0)
```

* The **last** line of our program provides the return code that will be returned to the calling interpreter.
* On Unix, by convention a value of 0 means success, and any other value means failure.
* There are [several exit functions in Python](https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/), but sys.exit() is the right one to use.
* Last but not least, there should be no blank lines, nor anything else after that function call. This is the end!

## Other tools output:
Here's an example of the [what](https://www.freebsd.org/cgi/man.cgi?query=what)([1](https://www.freebsd.org/cgi/man.cgi?query=intro&sektion=1)) command output on our program:
```
# what hello_world.py
hello_world.py:
         $Id: hello_world - say hello to the world v1.0.0 (May 13, 2021) by Hubert Tournier $
```

And one for the [ident](https://www.freebsd.org/cgi/man.cgi?query=ident)([1](https://www.freebsd.org/cgi/man.cgi?query=intro&sektion=1)) command output on our program:
```
# ident hello_world.py
hello_world.py:
     $Id: hello_world - say hello to the world v1.0.0 (May 13, 2021) by Hubert Tournier $
```

### Checking our source code correctness and compliance with the [PEP 8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/):
Just like you would do with [lint](http://www.catb.org/~esr/jargon/html/L/lint.html) for [C language](http://www.catb.org/~esr/jargon/html/C/C.html) code, you can do that for Python with the [pylint package](https://pypi.org/project/pylint/):
```
# pylint hello_world.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

### Checking our source code security:
You can do that with the [bandit package](https://pypi.org/project/bandit/):
```
# bandit -r hello_world.py
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.8.9
[node_visitor]  INFO    Unable to find qualified name for module: hello_world.py
Run started:2021-05-13 22:10:17.348437

Test results:
        No issues identified.

Code scanned:
        Total lines of code: 8
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
        Total issues (by confidence):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
Files skipped (0):
```

### Formatting our source code in a conventional way:
Just like you would do with [cb](https://www.freebsd.org/cgi/man.cgi?query=cb&manpath=Unix+Seventh+Edition) for [C language](http://www.catb.org/~esr/jargon/html/C/C.html) code, though unnecessary for our simple example, you can do that with the [black package](https://pypi.org/project/black/):
```
# black hello_world.py
All done! ✨ 🍰 ✨
1 file left unchanged.
```

### Analyzing the minimum version of Python required for running the program:
You can do that with the [vermin package](https://pypi.org/project/vermin/):
```
# vermin hello_world.py
Minimum required versions: 2.0, 3.0
```
That will be useful when we'll talk about [making installation packages](https://packaging.python.org/tutorials/packaging-projects/) later.
