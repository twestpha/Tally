################################################################################
# Database Interface
# Defines the method in which to query and receive data from the database,
# as well as starting and managing the server software itself.
################################################################################

import subprocess

from printer import PrintInfo
from printer import PrintError

class DataBaseInterface:
    def __init__(self):
        pass

    def StartServer(self):
        PrintInfo("Starting server")
        self.server = subprocess.Popen(self.configdict["serverpath"] + " " + self.configdict["serverargs"], shell=False)
        PrintInfo("Server started with pid %d" % self.server.pid)

    def StopServer(self):
        self.server.terminate()
        PrintInfo("Server stopped")
