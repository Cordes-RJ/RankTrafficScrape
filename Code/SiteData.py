# -*- coding: utf-8 -*-
import Constants

def writeToSiteData(SiteInfoList):
    SiteInfoList = filterEmptySiteInfo(filterEmptySiteInfo)
    f = open(Constants.sitedatapath, 'a')
    for si in SiteInfoList:
        print(si)
        f.write("\n" + si.toCSVRow())
    f.close()
    
def filterEmptySiteInfo(SiteInfoList):
    idx= 0
    while idx < len(SiteInfoList):
        if SiteInfoList[idx].FtoScrape:
            idx+=1
        else:
            del SiteInfoList[idx]
    return SiteInfoList