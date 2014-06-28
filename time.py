# -*- coding: cp936 -*-
import re
import os
import sys

class Day:
    """
    一个关于日期的类
        """
    def __init__(self):
        self.mouthDayRun = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.mouthDayPing = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    """
    判断是否为闰年
        """
    def judgeRun(self, year):
        if year % 100 == 0:
            if year % 4 == 0:
                return True
            else:
                return False
        if year % 4 == 0:
            return True
        else:
            return False
    def parseDay(self, day):
        year = int(day[0: 4])
        mouth = int(day[4: 6])
        day = int(day[6:])
        return [year, mouth, day]
    """
    @param now string 20140521
    @param after int 3
    @return [[]]
    得到now 以后的 after 天的日期
        """
    def getAfterDay(self, now, after):
        year, mouth, day = self.parseDay(now)
        
        currentMouth = []
        if self.judgeRun(year) == True:
            currentMouth = self.mouthDayRun
        else:
            currentMouth = self.mouthDayPing
            
        result = []
        for i in xrange(1, after + 1):
            day += 1
            if day > currentMouth[mouth - 1]:
                day = 1
                mouth += 1
            if mouth > 12:
                mouth = 1
                year += 1
            result.append([year, mouth, day])
        return result
    """
    @param now string 20140521
    @param after int 3
    @return [[]]
    得到now 以后的 befer 天的日期
        """
    def getBeferDay(self, now, befer):
        year, mouth, day = self.parseDay(now)
        
        currentMouth = []
        if self.judgeRun(year) == True:
            currentMouth = self.mouthDayRun
        else:
            currentMouth = self.mouthDayPing
        result = []
        for i in xrange(1, befer + 1):
            day -= 1
            if day == 0:
                mouth -= 1
                day = currentMouth[mouth - 1]
            if mouth == 0:
                mouth = 12
                year -= 1
            result.append([year, mouth, day])
        return result
        

if __name__ == "__main__":
    day = Day()
    
    print day.getBeferDay("20141004", 7)
    print day.getAfterDay("20141004", 7)
