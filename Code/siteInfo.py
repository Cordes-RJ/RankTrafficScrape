# -*- coding: utf-8 -*-

class siteInfo:
    def __init__(self):
        self.name = ""
        self.FtoScrape = True # failure to scrape
        self.TrafficViews = 0 # views per day
        self.TrafficVisits = 0 # visits per day
        self.TrafficSessions = 0 # sessions per day
        self.Revenue = 0 # advertising revenue per day
        self.TrafficSourceSearch = 0 # traffic from search per day
        self.TrafficSourceDirect = 0 # traffic from direct per day
        self.TrafficSourceRefs = 0 # traffic from referrals per day
        self.UEviewsPerSession = 0 # user engagement, page views per session
        self.UESessionDuration = 0 # user session duration
        self.UEbounce = 0 # Bounce rate %
        self.alexaRank = 0 # alexa rank
    def toCSVRow(self): # returns siteinfo as 
        items = [self.name,self.FtoScrape ,self.TrafficViews ,self.TrafficVisits ,self.TrafficSessions, self.Revenue ,self.TrafficSourceSearch ,self.TrafficSourceDirect ,self.TrafficSourceRefs ,self.UEviewsPerSession ,self.UESessionDuration ,self.UEbounce,self.alexaRank]
        csvBlobString = ""
        for item in items:
            csvBlobString += str(item) + ","
        return csvBlobString
    def Parse(self,text):
        self.FindName(text)
        self.FindtrafficAndUEstats(text)
        self.FindtrafficSources(text)
        self.FindAdvertisingAndTrafficStats(text)
        self.FtoScrape = False
    def FindName(self,text):
        adelimiter = "Latest statistics for <strong>"
        bdelimiter = "</strong>"
        self.name= findStrangeDatum(text,adelimiter,bdelimiter)
    def findTrafficSessions(self,sessionCtstring):
        check = {
                "Thousand":1000, 
                "Million":1000000, 
                "Billion":1000000000,
                "Trillion":1000000000000
                }
        for i in check.keys():
            if sessionCtstring.find(i) != -1:
                self.TrafficSessions = (float(sessionCtstring[0:len(sessionCtstring)-len(i)-1]) * check[i])/30
    def FindtrafficAndUEstats(self,text):
        dataList = findStrangeData(text,"<span class=\"infobox-data-number\">","</span>",0)
        self.findTrafficSessions(dataList[1])
        self.alexaRank = float(dataList[2])
        self.UEviewsPerSession = float(dataList[3])
        self.UESessionDuration = dataList[4]
        self.UEbounce = float((dataList[5])[0:len(dataList[5])-1])/100
    def findtrafficSource(self,text,sourceType,start):
        h = text.find(sourceType,start)
        i = text.find("y: ",h)
        j = text.find("\n",i)
        return text[i+3:j] 
    def FindtrafficSources(self,text):
        f = text.find("What percentage of visits to this site")
        g = text.find('Traffic sources',f)
        sourceTypes =["'Search'","'Direct'","'Referrals'"]
        sourceValues = []
        for sourceType in sourceTypes:
            sourceValues.append(self.findtrafficSource(text,sourceType,g))
        self.TrafficSourceSearch = float(sourceValues[0])/100
        self.TrafficSourceDirect = float(sourceValues[1])/100
        self.TrafficSourceRefs = float(sourceValues[2])/100
    def findAdvertisingAndTrafficStat(self,text,statType,start):
        h = text.find(statType, start)
        i = text.find("<span class=\"badge badge-info\">",h+len(statType))
        j = text.find("</span>",i)
        return text[i+31:j]
    def findRevenue(self, theString):
        check = {
                "Thousand per day":1000, 
                "Million per day":1000000, 
                "Billion per day":1000000000,
                "Trillion per day":1000000000000
                }
        for i in check.keys():
            if theString.find(i) != -1:
                self.Revenue = float(theString[2:len(theString)-len(i)-1]) * check[i]
                return
        self.Revenue = float(theString[2:len(theString)-len("per day")-1])
    def findVisits(self, theString):
        check = {
                "Thousand visits / day":1000, 
                "Million visits / day":1000000, 
                "Billion visits / day":1000000000,
                "Trillion visits / day":1000000000000
                }
        for i in check.keys():
            if theString.find(i) != -1:
                self.TrafficVisits = float(theString[0:len(theString)-len(i)-1]) * check[i]
                return
        self.TrafficVisits = float(theString[0:len(theString)-len("visits / day")-1])
    def findPageviews(self, theString):
        check = {
                "Thousand pageviews / day":1000, 
                "Million pageviews / day":1000000, 
                "Billion pageviews / day":1000000000,
                "Trillion pageviews / day":1000000000000
                }
        for i in check.keys():
            if theString.find(i) != -1:
                self.TrafficViews = float(theString[0:len(theString)-len(i)-1]) * check[i]
                return
        self.TrafficViews = (theString[0:len(theString)-len("pageviews / day")-1])
    def FindAdvertisingAndTrafficStats(self,text):
        g = text.find("<td><b>Estimated Valuation</b></td>")
        statTypes =["<td>Advertising revenue per day:</td>","<td>Estimated visits per day:</td>","<td>Estimated pageviews per day:</td>"]
        statValues = []
        for statType in statTypes:
            statValues.append(self.findAdvertisingAndTrafficStat(text,statType,g))
        self.findRevenue(statValues[0])
        self.findVisits(statValues[1])
        self.findPageviews(statValues[2])

def findStrangeDatum(text,adelimiter,bdelimiter):
    a =text.find(adelimiter)
    b = text.find(bdelimiter,a)
    return text[a+len(adelimiter):b]


def findStrangeData(text,adelimiter,bdelimiter,start):
    List = []
    x = True
    a = start
    while x:
        b = text.find(adelimiter,a)
        c = text.find(bdelimiter,b)
        if b == -1 or c == -1:
            x = False
        else:
            List.append(text[b+len(adelimiter):c])
            a = c
    return List
"""
import utilWeb

b= utilWeb.getResponseText("https://www.rank2traffic.com/sciencedirect.com", "Just testing", 5)
m = siteInfo()
m.Parse(b)
z = [m]
"""
