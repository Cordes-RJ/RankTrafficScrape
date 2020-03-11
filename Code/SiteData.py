# -*- coding: utf-8 -*-
import Constants

def writeToSiteData(SiteInfoList):
    f = open(Constants.sitedatapath, 'a')
    for si in SiteInfoList:
        if si.toCSVRow() > len(15): 
            f.write("\n" + si.toCSVRow())
    f.close()
    