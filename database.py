import subprocess

from printer import PrintInfo
from printer import PrintError

class DataBaseInterface:
    def __init__(self, configpath):
        configfile = open(configpath, 'r')
        self.configdict = {}
        for line in configfile:
            if("=") in line:
                key = line.split("=")[0].strip()
                value = line.split("=")[1].strip()
                self.configdict[key] = value

        configfile.close()

    def StartServer(self):
        PrintInfo("Starting server")
        self.server = subprocess.Popen(self.configdict["serverpath"] + " " + self.configdict["serverargs"], shell=False)
        PrintInfo("Server started with pid %d" % self.server.pid)

    def SomethingElse(self):
        PrintInfo("LAKSJDKLJASKLDJKLSJD")

    def StopServer(self):
        self.server.terminate()
        PrintInfo("Server stopped")
