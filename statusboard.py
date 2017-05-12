#!/usr/bin/env python3

import sys

from statusboard.statusboard import Statusboard
from statusboard.logger import Logger

# Create the application-wide logger using default settings
log = Logger()


if __name__ != "__main__":
    sys.stderr.write("Statusboard is a standalone application. Don't try to import it.")
    quit(1)


# Create the default Statusboard and go into the board loop
board = Statusboard()
board.run()

