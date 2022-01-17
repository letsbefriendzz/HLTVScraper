from bs4 import BeautifulSoup

class player:
    name = ""
    rating = 0
    dpr = 0
    kast = 0
    impact = 0
    adr = 0
    kpr = 0

    def __init__(self, newname, newrating, newkpr, newhs, newmaps, newdpr, newrc):
        self.name = str(newname)
        self.rating = str(newrating)
        self.kpr = str(newkpr)
        self.hs = str(newhs)
        self.maps = str(newmaps)
        self.dpr = str(newdpr)
        self.rc = str(newrc)

    def PrintPlayer(self):
        print("Name:\t\t\t" + self.name)
        print("Rating 2.0:\t\t" + self.rating)
        print("Deaths/Round:\t\t" + self.kpr)
        print("KAST:\t\t\t" + self.hs)
        print("Impact:\t\t\t" + self.maps)
        print("ADR:\t\t\t" + self.dpr)
        print("KPR:\t\t\t" + self.rc)