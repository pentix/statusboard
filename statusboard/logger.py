import sys
import datetime

LOGLEVEL_DEBUG = 3
LOGLEVEL_INFO = 2
LOGLEVEL_WARNING = 1
LOGLEVEL_ERROR = 0

LOGLEVELS = ["ERROR", "WARN ", "INFO ", "DEBUG"]


class Logger():
    def __init__(self, stderr=sys.stderr, loglevel=LOGLEVEL_INFO):
        self.stderr = stderr
        self.loglevel = loglevel

    def __out(self, s, level):
        self.stderr.write("[{}] [{}] {}\n".format(datetime.datetime.now(),
                                                LOGLEVELS[level],
                                                s))


    def debug(self, s):
        if self.loglevel >= LOGLEVEL_DEBUG:
            self.__out(s, LOGLEVEL_DEBUG)

    def info(self, s):
        if self.loglevel >= LOGLEVEL_INFO:
            self.__out(s, LOGLEVEL_INFO)

    def warning(self, s):
        if self.loglevel >= LOGLEVEL_WARNING:
            self.__out(s, LOGLEVEL_WARNING)

    def error(self, s):
        if self.loglevel >= LOGLEVEL_ERROR:
            self.__out(s, LOGLEVEL_ERROR)
