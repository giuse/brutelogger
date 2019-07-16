import sys, os, time

class BruteLogger:
    """ A brutish file logger for when you just need to `tee` your screen.
        Forks `stdout` to multiple handlers.

        Logging done right should use `logging`, or the wonderful `loguru`.

        Goal of this library is instead to offer a brute redirect of
        everything that comes on screen to multiple handlers, typically
        the original terminal and a file. The goal is not logging, but
        maintaining a hard copy of the terminal output in case of failure
        (or future processing).

        The original use case includes for example having multiple processes
        running asynchronously, each calling a C library which `printf()`s
        to screen some important algorithm statistics.
        BruteLogger redirects everything such that what is seen on screen is
        copied to the file (think of `tee`). Statistics can be later easily
        retrieved using regular expressions, for example for plotting purposes.
    """

    def __init__(self, *handlers):
        """NOTICE: the order in which handlers are declared could be important!
           See line with `return res` below to verify weather it is for you.
        """
        self.handlers = handlers

    def __getattr__(self, attr_name, *args, **kwargs):
        def wrapper(*wr_args, **wr_kwargs):
            """Delegate all calls to handlers, return last response"""
            # Initially inspired by https://stackoverflow.com/a/16551730/6392246
            for handl in self.handlers:
                res = getattr(handl, attr_name, *args, **kwargs)(*wr_args, **wr_kwargs)
            return res # return output from last handler -- hope that's fine with you!
        return wrapper

    @staticmethod
    def save_stdout_to_file(fname=time.strftime("%y%m%d_%H%M.log"), path='logs',
                            mode='w', encoding='utf8', also_stderr=False):
        """Redirect sys.stdout to a BruteLogger copying to console + logfile"""
        if not os.path.exists(path): os.makedirs(path)
        full_name = os.path.join(path, fname)
        file_desc = open(full_name, mode=mode, encoding=encoding, buffering=1)
        sys.stdout = BruteLogger(sys.stdout, file_desc)
        if also_stderr: sys.stderr = sys.stdout
