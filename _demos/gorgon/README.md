# gorgon
gorgon is our first example of Unix [filter](http://www.catb.org/jargon/html/F/filter.html).

As [Eric S. Raymond](https://en.wikipedia.org/wiki/Eric_S._Raymonda) says in [The Jargon File](http://www.catb.org/jargon/html/index.html):
>> \[a filter is] A program that processes an input data stream into an output data stream in some well-defined way, and does no I/O to anywhere else except possibly on error conditions;
>> one designed to be used as a stage in a pipeline

Thus a filter program is intended to be used in a command pipeline, for example between [cat](https://www.freebsd.org/cgi/man.cgi?query=cat) and [tee](https://www.freebsd.org/cgi/man.cgi?query=tee):

```Shell
cat inputfile | gorgon.py | tee result.txt
```

This Unix [plumbing](http://www.catb.org/jargon/html/P/plumbing.html) is an essential part of the operating system!

As the "AT&T Unix System V Release 3.2 Programmer's Guide, Vol. I" manual said in my 1989 edition:
>> **UNIX System Philosophy Simply Stated**
>>
>> For as long as you are writing programs on a UNIX system you should keep this motto hanging on your wall:
>>
>> \* * * * * * * * * * * * * * * * * * * *
>> 
>> \* Build on the work of others *
>> 
>> \* * * * * * * * * * * * * * * * * * * *
>>
>> Unlike computer environments where each new project is like starting with a blank canvas, on a UNIX system a good percentage of any programming effor is lying there in **bins**, and **lbins**, and **/usr/bins**, not to mention **etc**, waiting to be used.
>> 
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
* We have a special case here with an argument called "\_" which Python uses to explicitely state that it will be unused.
* The function here returns a string value, but it could have been any other type, including complex structures, and even multiple return values!

```Python
for line in sys.stdin:
    for word in line.rstrip().split(" "):
        print(petrification(word) + " ", end="")
    print()
```

* The first line reads a text line in a special file called STDIN (from STanDard INput), which will either be the output of the previous command in the command pipeline, or the user input if your filter is the first part of a command pipeline.
* There are 2 other special files: STDOUT (STanDard OUTput) and STDERR (STanDard ERRor output).
* When you print() you are in fact writing to STDOUT, which will either be the next command in the command pipeline, or the terminal you use if your filter is the last part of a command pipeline. As you can see in the Python manual, the [print()](https://docs.python.org/3/library/functions.html#print) function as a default parameter "file=sys.stdout".
* The STDERR channel is to be used for error messages, thus separating them from normal output, and avoiding polluting it if you are redirecting to a file (you do that by ending your command pipeline with "> filename").
* The next line splits the line in words (separated by spaces) and removes the newline character at the end of each line with the rstrip() function (as in Right Strip).
* The next line process the input word into our previously defined function and prints it without adding a newline (so that all words stay on the same line). This is done by changing print() default parameter "end='\n'" to "end=''".

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

## Some historical notes:
[Gorgons](https://en.wikipedia.org/wiki/Gorgon) were creatures in Greek mythology which are described as having hair made of living, venomous snakes and horrifying visages that turned those who beheld them to stone. The most famous one, [Medusa](https://en.wikipedia.org/wiki/Medusa), was slain by Perseus.

I said on the front page of the project that there would be no [Demogorgon](https://en.wikipedia.org/wiki/Demogorgon#Dungeons_&_Dragons) here, but we do have this demos/gorgon instead :-)

There will be other [easter eggs](http://www.catb.org/jargon/html/E/Easter-egg.html) like this though this project. That's another tradition we want to honor!

On the lore side, it's interesting to note that the Demogorgon was one of the monsters of the classical [NetHack](https://en.wikipedia.org/wiki/NetHack) game, which itself was a descendant of the mythical [Rogue](https://en.wikipedia.org/wiki/Rogue_(video_game)) and [Hack](https://en.wikipedia.org/wiki/Hack_(video_game)) games, which were included in BSD Unix and many other versions after that.

Perhaps someone will reimplement these important milestones in video gaming history for the project?
