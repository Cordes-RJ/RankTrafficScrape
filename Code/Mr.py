# -*- coding: utf-8 -*-

import Constants
import SiteList
import rankTrafficScrape as rts
import SiteData
import listener

class Manager:
    def __init__(self):
        self.Run()
    def Delegate(self):
        print("> Getting Site List...")
        sitelist = SiteList.GetSiteList(Constants.sitelistpath)
        print("> Scraping Politely...")
        DataList = rts.Scraper().Scrape(sitelist,"Just testing some stuff for research purposes--trying to be as polite as possible--contact at rj.cordes@cogsec.org", 4)
        print("> Writing SiteData to CSV...")
        SiteData.writeToSiteData(DataList)
        print(" > Cleaning Up...")
        SiteList.EmptyContents(Constants.sitelistpath)
    def Run(self):
        EAR = listener.listener(Constants.sitelistpath, 30)
        while True:
            if EAR.listen():
                print("> Running Scrape...")
                self.Delegate()
                print("> Scrape Concluded")
            else:
                EAR.WaitAndListen()