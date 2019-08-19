import sys, os, time

class BruteLogger:
    """ A brutish file logger for when you just need to `tee` your screen.

        NOTICE: Logging done right should use `logging`, or the wonderful `loguru`.

        This library offers instead a brute redirect of everything that comes on
        screen to multiple handlers, typically including the original terminal and
        a log file. The goal is to maintain a hard copy of the output in case of
        failure, or for future processing.
        For example, the original use case included multiple processes running
        asynchronously, each calling a C library which used `printf()` to deliver
        important algorithm statistics. These became easy to retrieve from the log
        file using regular expressions.
    """

    def __init__(self, *handlers):
        """Initialize a BruteLogger on a set of handlers.
           NOTICE: the order in which handlers are declared could be important,
           see the return of the `wrapper` inside `__getattr__` below.
        """
        if len(handlers) == 1 and type(handlers[0]) is list:
            self.handlers = handlers[0]
        else:
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
        """Redirect sys.stdout to a BruteLogger copying to stdout + logfile"""
        if not os.path.exists(path): os.makedirs(path)
        full_name = os.path.join(path, fname)
        file_desc = open(full_name, mode=mode, encoding=encoding, buffering=1)
        sys.stdout = BruteLogger(sys.stdout, file_desc)
        if also_stderr: sys.stderr = sys.stdout
