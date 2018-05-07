import time
from database import DataBaseInterface
from downloader import Downloader

# Global Settings dictionary
settings = {}
configfile = open("config.txt", 'r')
for line in configfile:
    if("=") in line:
        key = line.split("=")[0].strip()
        value = line.split("=")[1].strip()
        settings[key] = value
configfile.close()

# Setting up objects
downloader = Downloader()

# Main program loop
while(True):
    downloader.DownloadPage("www.google.com")

    time.sleep(float(settings["delaytime"]))

# Database Setup
# db = DataBaseInterface("config.txt")
# db.StartServer()
# db.StopServer()
