# logging1
Now that we are ready to start coding, we'll soon need to either confirm that our program performs as intended or chase [bugs](http://www.catb.org/jargon/html/B/bug.html).

If you want something more reliable than [shotgun debugging](http://www.catb.org/jargon/html/S/shotgun-debugging.html), and less complex than using a debugger, you'll probably want to spread debugging print() messages through your code.

Instead of doing that, Python provides a full featured [logging library](https://docs.python.org/3/library/logging.html), that will advantageously replace these print() messages.

You'll even be able to keep your debugging code in your program and just vary the logging level to make them appear or not!

So let's explain the new code constructs since our hello_world program.

## Code commentary:
```Python
import logging
import os
```

* The logging library is included with the "import logging" statement.
* We also import the os library in order to help get the name of the running program, though it's not at all mandatory.

```Python
def show_logging_levels():
    """Prints a message at each logging level"""
    logging.debug("Debug message (detailed diagnostic information)")
    logging.info("Info message (things working as expected)")
    logging.warning("Warning message (things still working as expected, but potential for future errors)")
    logging.error("Error message (unable to perform some function)")
    logging.critical("Critical message (program unable to continue)")
```

* This function is just a showcase for the 5 logging functions you can call in your programs, with some explanations on the situation  requiring their use.
* Please note that the function names are all lowercase. That's a common source of mistakes as we'll see later on.
* A critical level error should go with an immediate sys.exit() function call with a non zero return code.
* For error level ones, your program should **ultimately** exit with a non zero code. 

```Python
PROGRAM_NAME = os.path.basename(sys.argv[0])
CONSOLE_LOG_FORMAT = PROGRAM_NAME + ": %(levelname)s: %(message)s"
logging.basicConfig(format=CONSOLE_LOG_FORMAT, level=logging.DEBUG)
logging.disable(logging.INFO)
```

* The first line gets the name of the running program, which is the first argument on the command line.
* The command line is available through the sys.argv table, with its full pathname in the first cell. The os.path.basname() call helps get rid of the directory part.
* The logging module has pre-defined variables with your module name, filename and pathname, but they are related to your source code file rather than your program. If you make a multiple source files program, they probably won't work as intended.
* The second line defines the format of the messages destined to the console. The logging facility also enables you to log to a file, in which case you would probably want to prefix the format with the date & time of the error (with "%(asctime) " at the beginning of the format string).
* The logging.basicConfig call is supposed to be placed at the beginning of your main code, just after your functions definitions.
* The logging level must be set to logging.DEBUG level if you intend to modify it later on to higher levels (or else it won't work).
* The next line is supposed to follow immediately to set the normal logging level to WARNING or higher. For a production release program you don't want to see DEBUG or INFO level messages...

```Python
logging.disable(logging.NOTSET)
```

* The line above will reset the logging level to DEBUG messages or higher (NOTSET is the level below DEBUG).
* This is what you need to activate the debugging mode!
* Usually you do this when there's a command line option, environment variable or configuration file item instructing you to do so, but we'll see all these things later on.

```Python
ERROR_MESSAGE = "FMH!"
logging.error("Message: %s", ERROR_MESSAGE)
CRITICAL_ERROR_MESSAGE = "Fandango on core :-("
logging.critical("Message: %s", CRITICAL_ERROR_MESSAGE)
```

* Here are some closing examples showing how to pass variable content to your logging function calls.
* The strings themselves are constants, thus their all caps names.
* I leave it as an exercise to you to get the meaning of these classical error messages in [The Jargon File](http://www.catb.org/jargon/html/index.html) :-)

## The program's output:
```
# logging1.py
logging1.py: WARNING: Warning message (things still working as expected, but potential for future errors)
logging1.py: ERROR: Error message (unable to perform some function)
logging1.py: CRITICAL: Critical message (program unable to continue)

Now changing the logging level to DEBUG and above
logging1.py: DEBUG: Debug message (detailed diagnostic information)
logging1.py: INFO: Info message (things working as expected)
logging1.py: WARNING: Warning message (things still working as expected, but potential for future errors)
logging1.py: ERROR: Error message (unable to perform some function)
logging1.py: CRITICAL: Critical message (program unable to continue)

Some examples with parameters in error messages:
logging1.py: ERROR: Message: FMH!
logging1.py: CRITICAL: Message: Fandango on core :-(
```

## Other tools output:

### Checking our source code correctness and compliance with the [PEP 8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/):
Using the [pylint package](https://pypi.org/project/pylint/):
```
# pylint logging1.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

### Checking our source code security:
Using the [bandit package](https://pypi.org/project/bandit/):
```
# bandit -r logging1.py
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.8.9
[node_visitor]  INFO    Unable to find qualified name for module: logging1.py
Run started:2021-05-15 10:30:30.350050

Test results:
        No issues identified.

Code scanned:
        Total lines of code: 33
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

### Analyzing the minimum version of Python required for running the program:
Using the [vermin package](https://pypi.org/project/vermin/):
```
# vermin logging1.py
Minimum required versions: 2.4, 3.0
```
