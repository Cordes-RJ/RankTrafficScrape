# -*- coding: utf-8 -*-
import pandas as pd

def ReadInCSV(path):
    x = pd.read_csv(path)
    return x.dropna().values.tolist()

def CleanList(siteList):
    idx = 0
    while idx < len(siteList):
        if siteList[idx][1]:
            siteList[idx] = siteList[idx][0]
            idx+=1
        else:
            del siteList[idx]
    return siteList
        
def GetSiteList(path):
    return CleanList(ReadInCSV(path))

def EmptyContents(path):
    open(path, 'w').close()
"""
import Constants

x = GetSiteList(Constants.sitelistpath)
"""