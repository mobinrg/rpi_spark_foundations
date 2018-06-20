# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) 2018 Kunpeng Zhang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# #########################################################
#
#    Moving Average
#    2018.4.01
# 
class MovingAvgCalculator:
    _list = None
    _lastSum = None
    count = None
    lastMA = None

    def __init__(self, count = 15):
        self.count = count
        self.clear()

    def clear(self):
        self._lastSum = 0
        self._list = []
        self.lastMA = 0

    def addValue(self, newValue):
        self._list.append( newValue )
        self._lastSum += newValue
        if len(self._list)>=self.count:
#             print self._list, self.count, len(self._list)
            self.lastMA = self._lastSum / self.count
            self._lastSum = self._lastSum - (self._list.pop(0))
            return self.lastMA
        else:
            return None

# #########################################################
#
#    Moving Average 2
#    2018.4.01
# 
class AvgCalculator:
    _maxValue = None
    _minValue = None
    _avgSumValue = None
    _valueCount = None
    count = None
    lastAvgValue = None

    def __init__(self, count = 15):
        self.count = count
        self._maxValue = 0
        self._minValue = 0
        self._avgSumValue = 0
        self._valueCount = 0
        self.lastAvgValue = 0

    def addValue(self, newValue):
        if newValue > self._maxValue: self._maxValue = newValue
        if newValue < self._minValue: self._minValue = newValue
        self._avgSumValue += newValue
        self._valueCount += 1

        if self._valueCount >= self.count :
            self.lastAvgValue = (self._avgSumValue - self._maxValue - self._minValue) / (self._valueCount - 2)
            self._maxValue = 0
            self._minValue = 0
            self._avgSumValue = 0
            self._valueCount = 0
            return self.lastAvgValue

        return None


if __name__ == "__main__":
    ma = MovingAvgCalculator(5)
    item_str1 = "%(in)d\t%(ma)d"
    item_str2 = "%(in)d\t%(ma)s"
    print("MovingAvgCalculator")
    print("NUM\tMA")
    print("----\t----")
    for n in range(1,15):
        newAvg = ma.addValue(n)
        if newAvg != None:
            print(item_str1 % {"in":n, "ma":newAvg})
        else:
            print(item_str2 % {"in":n, "ma":"N/A"})
            
    print("")
    ac = AvgCalculator(5)
    print("AvgCalculator")
    print("NUM\tMA")
    print("----\t----")
    for n in range(1, 30):
        newAvg = ac.addValue(n)
        if newAvg != None:
            print(item_str1 % {"in":n, "ma":newAvg})
        else:
            print(item_str2 % {"in":n, "ma":"N/A"})
