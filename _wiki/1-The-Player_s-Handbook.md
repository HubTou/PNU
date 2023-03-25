# [The Player's Handbook](https://en.wikipedia.org/wiki/Player%27s_Handbook)
So you decided to play with us, that's [insanely great](http://www.catb.org/jargon/html/I/insanely-great.html)!

If you are in just for fun, the first 3 steps below will be enough for the time being and you can safely skip all the other steps.

However, if you intend to take the full learning curve and eventually publish your work or submit it to the project, please keep on reading.

  * [Selection](#selection)
  * [Coding](#coding)
  * [Tests](#tests)
  * [Documentation](#documentation)
  * [Installation](#installation)
  * [Source code publication](#source-code-publication)
  * [Package publication](#package-publication)
  * [Maintenance](#maintenance)
  * [Referencing](#referencing)
  * [Commands flavours](#commands-flavours)

## Selection
* The first step is to decide on a Unix command to reimplement in Python 3.x.
* You can use our [suggested list](https://github.com/HubTou/PNU#suggested-tasks-and-progression) in the front page, pick one from our [Monster Manual](https://github.com/HubTou/PNU/wiki/The-Monster-Manual), or just go for any other one (even [from other operating systems](https://github.com/HubTou/PNU/wiki/Manual-of-the-Planes)!) that fits your whims and fancies.
* If you have selected a [POSIX command](https://pubs.opengroup.org/onlinepubs/9699919799/idx/utilities.html), you can start implementing the [POSIX.1](https://pubs.opengroup.org/onlinepubs/9699919799/nframe.html) version instead of the latest version available in your favourite Operating System. POSIX versions are simpler and more testing oriented.

## Coding
* If you are starting with Python & Unix, check [our tutorials](https://github.com/HubTou/PNU/blob/main/_demos/README.md) first.
* Aim to be compliant with the [PEP 8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).
  * Though it's a good read, you can also just check your code compliance with the [pylint](https://www.pylint.org/) utility, and learn as you go.
* Do your unit [tests](http://www.catb.org/jargon/html/T/test.html):
  * There you can use our very simple [debugging and logging tutorial](https://github.com/HubTou/PNU/tree/main/_demos/logging1), which we suggest.
  * Or the more complex Python [unit testing library](https://docs.python.org/3/library/unittest.html) or the third party [pytest](https://docs.pytest.org/) framework (check this [article](https://blog.j-labs.pl/2019/02/Pytest-why-its-more-popular-than-unittest) for advocacy on this later one).
* Last but not least, try to follow the [Pythonic](https://realpython.com/learning-paths/writing-pythonic-code/) way, that is to say using Python specific code constructs (loops, list comprehension and so on...).

As Mando says:
>> This is the way!

## Tests
There are 3 kind of tests that you should do:
* **Security checks**:
  * IT security is the concern of everyone. And it starts with the conception and the coding of your software (well even before with hardware or your compiler and interpreters, but [that's another story](https://dl.acm.org/doi/epdf/10.1145/358198.358210)).
  * You can check your code security with the [bandit package](https://pypi.org/project/bandit/) utility.
* **Back to back testing**:
  * You can write a [script](https://github.com/HubTou/b2bt/blob/main/README.5.md) for testing your new command against the installed one, if we don't already have one [available](https://github.com/HubTou/PNU/tree/main/tests).
  * We provide a dedicated tool, [b2bt](https://github.com/HubTou/b2bt), to ease making sure that the two commands are performing exactly the same, or as close as possible.
* **Portability testing**:
  * You should also test execution under Windows for the portability goal.
  * The same [b2bt](https://github.com/HubTou/b2bt) tool allows you to compare Windows results with those of your Unix machine.

## Documentation
* The traditional Unix way for documenting things is to write a [man](https://www.freebsd.org/cgi/man.cgi?query=man)ual page (in the newer and preferred [mdoc](https://www.freebsd.org/cgi/man.cgi?query=mdoc&sektion=7) or historical [man](https://www.freebsd.org/cgi/man.cgi?query=man&sektion=7) languages).
* If you intend to publish your code on GitHub, also write a README.md file (in the [GitHub flavour](https://guides.github.com/features/mastering-markdown/) of the [Markdown](https://en.wikipedia.org/wiki/Markdown) language).
* Though probably unneeded when it comes to documenting small Unix commands, if you feel like you could write a novel, consider using the [Read the Docs](https://readthedocs.org/) platform and the [Sphinx](https://www.sphinx-doc.org/) generation tool (which can even generate manual pages). Here's a [link to get you started](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html) if it's the path you choose.
* Nonetheless, [comparing different solutions for Unix Manuals](https://www.usenix.org/publications/login/october-2009-volume-34-number-5/fixing-standard-language-unix-manuals) shows that **mdoc is the way to go**. Check the following [page](https://mandoc.bsd.lv/mdoc/) for an introduction, a style guide, reference manuals and details about the mdoc language. 
* We provide mdoc man page and GitHub README.md skeletons in our project [template](https://github.com/HubTou/PNU/tree/main/_template) to help get you started.

## Installation
* Write an installation script or [Makefile](https://www.freebsd.org/cgi/man.cgi?query=makefiles) (check this excellent [tutorial](https://makefiletutorial.com/) for Makefiles) to install your commands and man pages.
* However, if you need something portable across multiple Operating Systems, you'll have to go for a Python package (more on this [later](https://github.com/HubTou/PNU/wiki/The-Player%27s-Handbook/_edit#package-publication)).
* We provide a rather complete generic Makefile in our project [template](https://github.com/HubTou/PNU/tree/main/_template) to help get you started (the one in the source code directory, not the one at the package level).

## Source code publication
* Select an [OSI-approved Open Source License](https://opensource.org/licenses) and put it in a License file.
* Eventually use [Black](https://github.com/psf/black), "The Uncompromising Code Formatter" utility, to reformat your code in a conventional way, hopefully improving readability by others.
* [Create a GitHub account](https://github.com/join?ref_cta=Sign+up).
* [Create a repository](https://docs.github.com/en/github/getting-started-with-github/quickstart/create-a-repo) and upload your code inside.
* [Create a release](https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github/managing-releases-in-a-repository) for a version of your code.
* Edit the repository details and add the [pnu-project](https://github.com/topics/pnu-project) topic, which will establish a soft link between your command and the project.

## Package publication
* Eventually, consider [making a pip package](https://packaging.python.org/tutorials/packaging-projects/) for your entry, so that it can be automatically installed on any Operating System supporting Python.
* To publish your package, you'll need to create an account on [PyPi](https://pypi.org/account/register/) and [TestPyPi](https://test.pypi.org/account/register/).
* We provide a [template](https://github.com/HubTou/PNU/tree/main/_template) with all the files required to make your own package. You can download a compressed archive file with everything inside in the assets of the [releases](https://github.com/HubTou/PNU/releases) section.

## Maintenance
* Check the [issues](https://guides.github.com/features/issues/) section of your GitHub repository for bug reports, documentation suggestions, new feature requests. and questions.
* If needed, correct things and make new releases.

## Referencing
* The PNU project itself doesn't include any code, beyond what we use for tutorials.
* Instead we provide an "empty" Python package with dependencies on the best tools identified through the [pnu-project](https://github.com/topics/pnu-project) GitHub topic or [pnu-project](https://pypi.org/search/?q=pnu-project) PyPi keyword.
* If there are multiple implementations to choose from for a peculiar utility, the one that will be referenced will be the first, most complete one. On your marks, get set, go!

## Commands flavours
* Sometimes there are incompatible flavours to choose for implementation, between [POSIX](https://en.wikipedia.org/wiki/POSIX), [System V](https://en.wikipedia.org/wiki/UNIX_System_V), [BSD](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution), [GNU](https://www.gnu.org/software/coreutils/), and others.
* The ideal would be to implement them all and use environment variables or command line options to choose between different commands behaviour.
* One such environment variable is the [POSIXLY_CORRECT](https://www.freebsd.org/cgi/man.cgi?query=environ&sektion=7) one for strict POSIX compatibility. Though not very pleasant (the GNU project call it [POSIX_ME_HARDER](https://www.gnu.org/prep/standards/html_node/Non_002dGNU-Standards.html) :smiley:), it exists and should be implemented.
* Beyond that, there are no standards or conventions that we know about for selecting a peculiar flavour.
* We suggest using the generic **FLAVOUR** or the specific **COMMAND_FLAVOUR** environment variables (where COMMAND is your command's name) with a case insensitive value such as *posix, unix* (for Research Unix), *sysv, bsd, gnu, linux, windows, plan9, inferno* to indicate the flavour to be used, with possible even more precise indications such as *unix:v6, bsd:freebsd, bsd:netbsd, bsd:openbsd, gnu:linux*, etc.
* But that would just be [the cherry on the cake](https://www.macmillandictionary.com/dictionary/british/the-cherry-on-the-cake)!
