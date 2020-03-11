# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import requests
import utilTime
import time
import random as rand

# a request func
def getResponseText(URL,headerTxt, timeout):
    headers = {"User-Agent": headerTxt}
    return requests.get(URL, headers=headers, timeout=timeout).text

def politelyScrape(objectList,URLbuildFunc, requestFunc, parseResponseFunc,headerTxt,timeout):
    parsed = []
    for i in objectList:
        url = URLbuildFunc(i)
        responseText = ""
        print("request sent")
        stopwatch = utilTime.StopWatch()
        responseText = requestFunc(url,headerTxt,timeout)
        t = stopwatch.stop()
        if responseText != "":
            parsed.append(parseResponseFunc(responseText))
        time.sleep(t * 1.1+rand.randint(0,5)/5) # being polite to server
        # we give the server 10% more time then it took to respond
    return parsed