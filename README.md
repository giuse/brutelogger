# brutelogger

A brutish file logger for when you just need to `tee` your screen. Forks `stdout` to multiple handlers.

## Disclaimer

Logging done right should use [`logging`](https://docs.python.org/3/library/logging.html), or the wonderful [`loguru`](https://github.com/Delgan/loguru).

## Installation

`pip install brutelogger`

## Usage

```python
from brutelogger import BruteLogger
BruteLogger.save_stdout_to_file()
# Everything on screen from now on will be copied to a
# timestamped file inside `./logs/`
```

More options:

```python
from brutelogger import BruteLogger
BruteLogger.save_stdout_to_file(path='captains.log', fname='stardate_41153.7',
                                mode='wb', encoding='utf8', also_stderr=True)
print("Our destination is planet Deneb IV")
# => outputs both to terminal and to file `captains.log/stardate_41153.7` (in binary)
```


## Applications

Goal of this library is to offer a brute redirect of everything that comes on screen to multiple handlers, typically the original terminal and a file. The goal is not logging, but maintaining a hard copy of the terminal output in case of failure (or future processing).

The original use case includes for example having multiple processes running asynchronously, each calling a C library which `printf()`s to screen some important algorithm statistics.
BruteLogger redirects everything such that what is seen on screen is copied to the file (think of `tee`). Statistics can be later easily retrieved using regular expressions, for example for plotting purposes.


## How does it work

Any function (or call) on the object (such as calling `sys.stdout.flush()` after using `BruteLogger.save_stdout_to_file()`) is propagated verbatim (with parameters) to each and all handlers.
This means that a call to `sys.stdout.flush()` will translate in calling `flush()` on both the terminal file handler and on the opened log file handler. Same goes for example with `close()` being called upon program termination.


## Todo

- Switching back `sys.__stdout__`
- Add / remove handlers
- Accessing handlers (e.g. calling `close()` only on the file log, not on the `__stdout__`)
