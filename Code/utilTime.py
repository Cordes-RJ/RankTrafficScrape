# -*- coding: utf-8 -*-

import time


class StopWatch:
    def __init__(self):
        self.time = time.time()
        self.Lap = 0
    def stop(self):
        return time.time() - self.time
    def getLapTimeString(self, roundTo):
        timeString = ""
        if self.Lap == 0:
            timeString = str(round(time.time() - self.time,roundTo)) + " seconds"
        else:
            timeString = str(round(time.time() - self.Lap,roundTo)) + " seconds"
        self.Lap = time.time()
        return timeString
    def getFullTimeString(self,roundTo):
        return str(round(time.time() - self.time,roundTo)) + " seconds"
