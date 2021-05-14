# gorgon
Gorgon is our first example of Unix [filter](http://www.catb.org/jargon/html/F/filter.html):

As [Eric S. Raymond](https://en.wikipedia.org/wiki/Eric_S._Raymonda) says in [The Jargon File](http://www.catb.org/jargon/html/index.html):
>> \[a filter is] A program that processes an input data stream into an output data stream in some well-defined way, and does no I/O to anywhere else except possibly on error conditions;
>> one designed to be used as a stage in a pipeline

Thus a filter program is intended to be used in a command pipeline, for example:

```Shell
cat inputfile | gorgon.py | tee result.txt
```

This Unix [plumbing](http://www.catb.org/jargon/html/P/plumbing.html) is an essential part of the operating system:

As the "AT&T Unix System V Release 3.2 Programmer's Guide, Vol. I" manual said in my 1989 edition:
>> **UNIX System Philosophy Simply Stated**
>> For as long as you are writing programs on a UNIX system you should keep this motto hanging on your wall:
>>
>> * * * * * * * * * * * * * * * * * * * * *
>> *                                       *
>> *      Build on the work of others      *
>> *                                       *
>> * * * * * * * * * * * * * * * * * * * * *
>>
>> Unlike computer environments where each new project is like starting with a blank canvas, on a UNIX system a good percentage of any programming effor is lying there in **bins**, and **lbins**, and **/usr/bins**, not to mention **etc**, waiting to be used.
>> The features of the UNIX system (pipes, processes, and the file system) contribute to this reusability, as does the history of sharing and contributing that extends back to 1969. Your risk missing the essential nature of the UNIX system if you don't put this to work.

So let's explain the new code constructs since our hello_world program.

## Code commentary:
```Python
def petrification(_):
    """Turns the input into stone"""
    return "stone"
```

* This is our first Python function :-)
* You'll notice the [docstring](https://www.python.org/dev/peps/pep-0008/#documentation-strings) comment right after the function definition.
* You should add docstrings for all **public** modules, functions, classes and methods, immediately after the def line.
* We have a special case here with an argument called "_" which means that we won't be using it.
* The function here returns a string value, but it could have been any other type, including complex structures, and even multiple return values!

```Python
for line in sys.stdin:
    for word in line.rstrip().split(" "):
        print(petrification(word) + " ", end="")
    print()
```

* TO BE DONE

## Other tools output:

### Checking our source code correctness and compliance with the [PEP 8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/):
Using the [pylint package](https://pypi.org/project/pylint/):
```
# pylint gorgon.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

### Checking our source code security:
Using the [bandit package](https://pypi.org/project/bandit/):
```
# bandit -r gorgon.py
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.8.9
[node_visitor]  INFO    Unable to find qualified name for module: gorgon.py
Run started:2021-05-14 07:57:00.403921

Test results:
        No issues identified.

Code scanned:
        Total lines of code: 14
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
Using the [black package](https://pypi.org/project/black/):
```
# black gorgon.py
reformatted gorgon.py
All done! ✨ 🍰 ✨
1 file reformatted.
```
You'll notice that Black insert an extra blank line before and after a function definition.

### Analyzing the minimum version of Python required for running the program:
Using the [vermin package](https://pypi.org/project/vermin/):
```
# vermin gorgon.py
Minimum required versions: 2.0, 3.0
```
