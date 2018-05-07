################################################################################
# Downloader
################################################################################

from urllib2 import urlopen
from urllib2 import Request

from sys import getsizeof

from printer import PrintError
from printer import PrintInfo

class Downloader:
    def __init__(self):
        self.downloadedbytes = 0

    def DownloadPage(self, url):
        req = Request(url, headers={'User-Agent' : "Magic Browser", "Accept" : "text/html", "Accept-Encoding" : "gzip"})
        html = urlopen(req).read()

        bytes = getsizeof(html)
        self.downloadedbytes += bytes
        PrintInfo("Downloaded url '%s'\n\tPage:\t%.2f Mb\n\tTotal:\t%.2f Mb" % (url, bytes / 1048576.0, self.downloadedbytes / 1048576.0))

        return html

        # PrintError("URL %s could not be read\n\tException:%s" % (url, e))
