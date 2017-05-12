import webview as wv
from .logger import Logger

class Statusboard():
    """Statusboard base class generating the interface and receiving data"""
    def __init__(self, name="default"):
        self.logger = Logger()
        self.logger.info("Initializing Statusboard: " + name)

        self.name = name


    def run(self):
        """Display the interface and start displaying information"""

        self.logger.info("Running Statusboard '{}'".format(self.name))
        wv.create_window("Statusboard", "templates/index.html", fullscreen=True)




