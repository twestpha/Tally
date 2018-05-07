import time
from database import DataBaseInterface
from downloader import Downloader

# need list of websites to download

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
    downloader.DownloadPage("https://www.reddit.com/r/heroesofthestorm/")
    downloader.DownloadPage("http://amove.tv/itn/")

    time.sleep(float(settings["delaytime"]))

    # break

# Database Setup
# db = DataBaseInterface("config.txt")
# db.StartServer()
# db.StopServer()
