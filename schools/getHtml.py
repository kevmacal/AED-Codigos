import time, urllib2
import sys

class manualScrapper():
    url = ''

    def __init__(self, category=''):
        self.url=category

    def gethtml(url):
        try:
            req = urllib2.Request(url)
            return urllib2.urlopen(req).read()
        except Exception, e:
            print e
            time.sleep(2)
            return ''

    #print gethtml(sys.argv[2])
    print sys.argv[2]
    f=open("tempo.xml","a")
    f.write(gethtml(sys.argv[2]))
    f.close()