# -*- coding: utf-8 -*-
import Constants

def writeToSiteData(SiteInfoList):
    SiteInfoList = filterEmptySiteInfo(SiteInfoList)
    f = open(Constants.sitedatapath, 'a')
    for si in SiteInfoList:
        f.write("\n" + si.toCSVRow())
    f.close()
    
def filterEmptySiteInfo(SiteInfoList):
    idx= 0
    while idx < len(SiteInfoList):
        if SiteInfoList[idx].FtoScrape:
            print("failed to scrape, check failedToParse.HTML")
            del SiteInfoList[idx]
        else:
            idx+=1
    return SiteInfoList