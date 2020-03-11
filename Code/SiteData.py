# -*- coding: utf-8 -*-
import Constants

def writeToSiteData(SiteInfoList):
    f = open(Constants.sitedatapath, 'a')
    for si in SiteInfoList:
        f.write("\n" + si.toCSVRow())
    f.close()
    