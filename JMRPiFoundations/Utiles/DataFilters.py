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

from .AvgCalculators import MovingAvgCalculator

###########################################
# Sample 3 axis moving average filter
#
class Sample3AxisMAFilter:
    _count = None
    maX = None
    maY = None
    maZ = None
    
    lastMA_X  = None
    lastMA_Y  = None
    lastMA_Z  = None

    def __init__(self, count = 15):
        self._count = count
        self.maX = MovingAvgCalculator(count)
        self.maY = MovingAvgCalculator(count)
        self.maZ = MovingAvgCalculator(count)
        
    def clear(self):
        self.accelMA_X.clear(self._count)
        self.accelMA_Y.clear(self._count)
        self.accelMA_Z.clear(self._count)
        
    def addSampleValue(self, x, y, z):
        self.lastMA_X = self.maX.addValue(x)
        self.lastMA_Y = self.maY.addValue(y)
        self.lastMA_Z = self.maZ.addValue(z)

        if self.lastMA_X != None and self.lastMA_Y != None and self.lastMA_Z !=None:
            return {"x":self.lastMA_X, "y":self.lastMA_Y, "z":self.lastMA_Z}
        else:
            return None

###########################################
# Filter base
#
class SampleFilter:
    value = 0.0
    def addSampleValue(self, newValue): raise "Did not implement this method"

###########################################
# Low-pass_filter
# See http://en.wikipedia.org/wiki/Low-pass_filter for details low pass filtering
class LowFilter(SampleFilter):
    _filterConstant = None

    def __init__(self, rate, cutoffFreq):
        dt = 1.0 / rate;
        RC = 1.0 / cutoffFreq;
        self._filterConstant = dt / (dt + RC);

    def addSampleValue(self, newValue):
        self.value = newValue * self._filterConstant + self.value * (1.0 - self._filterConstant);
        return self.value

###########################################
# High-pass_filter
# See http://en.wikipedia.org/wiki/High-pass_filter for details on high pass filtering
class HighFilter(SampleFilter):
    _filterConstant = None
    _lastSampleVal = None

    def __init__(self, rate, cutoffFreq):
        dt = 1.0 / rate;
        RC = 1.0 / cutoffFreq;
        self._filterConstant = RC / (dt + RC);
        self._lastSampleVal = 0.0

    def addSampleValue(self, newValue):
        self.value = self._filterConstant * (self.value + newValue - self._lastSampleVal);
        self._lastSampleVal = newValue;
        return self.value



###########################################
# 3 axis low filter
#
class LowFilter3Axis:
    lpX = None
    lpY = None
    lpZ = None

    def __init__(self, rate = 25.0, cutoffFreq = 1.0):
        self.lpX = LowFilter(rate, cutoffFreq)
        self.lpY = LowFilter(rate, cutoffFreq)
        self.lpZ = LowFilter(rate, cutoffFreq)
        
    def addSampleValue(self, x, y, z):
        return {    
            "x":self.lpX.addSampleValue(x), 
            "y":self.lpY.addSampleValue(y), 
            "z":self.lpZ.addSampleValue(z)
            }

###########################################
# 3 axis high filter
#
class HighFilter3Axis:
    hpX = None
    hpY = None
    hpZ = None

    def __init__(self, rate = 25.0, cutoffFreq = 1.0):
        self.hpX = HighFilter(rate, cutoffFreq)
        self.hpY = HighFilter(rate, cutoffFreq)
        self.hpZ = HighFilter(rate, cutoffFreq)
        
    def addSampleValue(self, x, y, z):
        return {    
            "x":self.hpX.addSampleValue(x), 
            "y":self.hpY.addSampleValue(y), 
            "z":self.hpZ.addSampleValue(z)
            }
