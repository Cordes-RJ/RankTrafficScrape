# -*- coding: utf-8 -*-
import utilWeb

def URLfromSiteName(siteName):
    return "https://www.rank2traffic.com/" + siteName

def requesterFunc(url,headerTxt,timeout):
    return utilWeb.getResponseText(url,headerTxt,timeout)

def parseSiteInfo(html):
    pass

class Scraper:
    def __init__(self):
        pass
    def Scrape(self, itemList, header, timeout):
        List = utilWeb.politelyScrape(itemList,URLfromSiteName,requesterFunc,parseSiteInfo,header,timeout)
        return List