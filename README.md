# BruteLogger

A brutish file logger for when you just need to `tee` your screen. Forks `stdout` to multiple handlers.

## Notice

Logging done right should use [`logging`](https://docs.python.org/3/library/logging.html), or the wonderful [`loguru`](https://github.com/Delgan/loguru).

## Installation

`pip install brutelogger`

## Usage

```python
from brutelogger import BruteLogger
BruteLogger.save_stdout_to_file()
# Everything on screen from now on will be copied
# to a timestamped file inside `./logs/`
```

More options:

```python
from brutelogger import BruteLogger
BruteLogger.save_stdout_to_file(path='captains_log', fname='stardate_41153.7',
                                mode='wb', encoding='utf8', also_stderr=True)
print("Our destination is planet Deneb IV")
# => outputs both to terminal and to file `captains_log/stardate_41153.7` (in binary)
```

See the implementation of `save_stdout_to_file` for advanced usage.


## Applications

This library offers instead a brute redirect of everything that comes on screen to multiple handlers, typically including the original terminal and a log file. The goal is to maintain a hard copy of the output in case of failure, or for future processing.

For example, the original use case included multiple processes running asynchronously, each calling a C library which used `printf()` to deliver important algorithm statistics. These became easy to retrieve from the log file using regular expressions.


## How does it work

Any function (call, message) on (/to) the object is propagated verbatim with parameters to each and all handlers.
For example, calling `BruteLogger.save_stdout_to_file()` such as calling `sys.stdout.flush()` after using 
This means that a call to `sys.stdout.flush()` will translate in calling `flush()` on both the terminal file handler and on the opened log file handler. Same goes for example with `close()` being called upon program termination.


## Todo

- Option to switch back `sys.__stdout__`
- Add / remove handlers
- Accessing handlers (e.g. calling `close()` only on the file log, not on the `__stdout__`)
