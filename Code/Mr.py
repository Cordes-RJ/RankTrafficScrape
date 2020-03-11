# -*- coding: utf-8 -*-

import Constants
import SiteList
import rankTrafficScrape as rts
import SiteData

class Manager:
    def __init__(self):
        pass
    def Delegate(self):
        sitelist = SiteList.GetSiteList(Constants.sitelistpath)
        DataList = rts.Scraper().Scrape(sitelist,"Just testing some stuff for research purposes--trying to be as polite as possible--contact at rj.cordes@cogsec.org", 4)
        SiteData.writeToSiteData(DataList)
        SiteList.EmptyContents(Constants.sitelistpath)
    
#%%
m = Manager().Delegate()