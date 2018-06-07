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

from JMMovingAvg import JMMovingAvg

###########################################
# Sample 3 axis moving average filter
#
class JMSample3AxisMAFilter:
    _count = 0
    maX = None
    maY = None
    maZ = None
    
    lastMA_X  = None
    lastMA_Y  = None
    lastMA_Z  = None

    def __init__(self, count = 15):
        self._count = count
        self.maX = JMMovingAvg(count)
        self.maY = JMMovingAvg(count)
        self.maZ = JMMovingAvg(count)
        
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
class JMSampleFilter:
    value = 0.0
    def addSampleValue(self, newValue): raise "Did not implement this method"

###########################################
# Low-pass_filter
# See http://en.wikipedia.org/wiki/Low-pass_filter for details low pass filtering
class JMLowFilter(JMSampleFilter):
    _filterConstant = 0.0

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
class JMHighFilter(JMSampleFilter):
    _filterConstant = 0.0
    _lastSampleVal = 0.0

    def __init__(self, rate, cutoffFreq):
        dt = 1.0 / rate;
        RC = 1.0 / cutoffFreq;
        _filterConstant = RC / (dt + RC);

    def addSampleValue(self, newValue):
        self._lastSampleVal = newValue;
        self.value = self._filterConstant * (self.value + newValue - self._lastSampleVal);
        return self.value
