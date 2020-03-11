# -*- coding: utf-8 -*-

import os
import time

# listener listens for changes
class listener:
    def __init__(self, path, waitTime):
        self.path = path
        self.waitTime = waitTime
    def listen(self):
        if os.path.getsize(self.path) == 0:
            return False
        return True
    def wait(self):
        time.sleep(self.waitTime)
    def WaitAndListen(self):
        x = True
        while x:
            print("> Waiting")
            self.wait()
            print("> Checking for Changes...")
            if self.listen():
                print("> Changes Found.")
                x = False
            print("> No Changes Found.")