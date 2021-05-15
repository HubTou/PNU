# logging1
text

So let's explain the new code constructs since our hello_world program.

## Code commentary:
```Python
import logging
import os
```

* text

```Python
def show_logging_levels():
    """Prints a message at each logging level"""
    logging.debug("Debug message (detailed diagnostic information)")
    logging.info("Info message (things working as expected)")
    logging.warning("Warning message (things still working as expected, but potential for future errors)")
    logging.error("Error message (unable to perform some function)")
    logging.critical("Critical message (program unable to continue)")
```

* text

```Python
PROGRAM_NAME = os.path.basename(sys.argv[0])
CONSOLE_LOG_FORMAT = PROGRAM_NAME + ": %(levelname)s: %(message)s"
logging.basicConfig(format=CONSOLE_LOG_FORMAT, level=logging.DEBUG)
logging.disable(logging.INFO)
```

* text

```Python
logging.disable(logging.NOTSET)
```

* text

```Python
ERROR_MESSAGE = "FMH!"
logging.error("Message: %s", ERROR_MESSAGE)
CRITICAL_ERROR_MESSAGE = "Fandango on core :-("
logging.critical("Message: %s", CRITICAL_ERROR_MESSAGE)
```

* text

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
