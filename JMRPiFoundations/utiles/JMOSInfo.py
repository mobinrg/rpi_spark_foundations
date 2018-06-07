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
# Author: Kunpeng Zhang
# 2018.5.31
#

import subprocess
from subprocess import check_output
import re

class JMOSInfo:

    def _cmd(self, cmdParams):
        cmd = subprocess.Popen( cmdParams, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        out,error = cmd.communicate() 
        return out.splitlines()

    def bytes2Human(self, n):
        """
            bytes2Unit(10000) => '9K'
            bytes2Unit(100001221) => '95M'
            from LUMA libs
        """
        symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if n >= prefix[s]:
                value = int(float(n) / prefix[s])
                return '%s%s' % (value, s)
        return "%sB" % n

    def getMemUsage(self):
        memory = self._cmd(['free'])

        cols = re.sub(r'(( )+|(\n)+)', " ", memory[1])
        cols = re.sub("(.*\:)", "", cols)
        cols = re.sub("\A\s+", "", cols)
        usage = cols.split(' ')
        return {
                 "total": int(usage[0]),
                 "used": int(usage[1]), 
                 "free": int(usage[2]), 
                 "shared": int(usage[3]), 
                 "buffers": int(usage[4]), 
                 "cached": int(usage[5]),
                 "usage": float(usage[1])/float(usage[0])
               }

    def getDiskUsage(self, dir ):
        disk = self._cmd(['df', dir])
    
        cols = re.sub(r'(( )+|(\n)+)', " ", disk[1])
        cols = re.sub("(.*\:)", "", cols)
        cols = re.sub("\A\s+", "", cols)
        usage = cols.split(' ')
        return { "total":int(usage[1]),
                 "used": int(usage[2]),
                 "available": int(usage[3]), 
                 "usage": float(usage[4].replace("%", "")) / 100, 
                 "mounted":usage[5]
                 }
    
    def getCPUInfo(self):
        cpu_count = self._cmd( ["grep","-c", "^processor", "/proc/cpuinfo"] )[0]
        cpu_info = self._cmd( ["cat", "/proc/cpuinfo", "|", "uniq"] )
        result = {"processor": int(cpu_count)}
        for i in cpu_info:
            item = re.sub(r'((\t)+|(\n)+)', "", i)
            info = item.split(': ')
            try:
                if info[0] != "processor": result[info[0].replace(" ", "_").lower()] = info[1]
            except:
                continue
        return result
        
    def getCPUsage(self):
        cpu = self._cmd(["grep", "cpu", "/proc/stat" ])

        cols = re.sub(r'(( )+|(\n)+)', " ", cpu[0])
        cols = re.sub("\A\s+", "", cols)
        usage = cols.split(' ')
        return ( float(usage[1]) + float(usage[3]) ) / ( float(usage[1]) + float(usage[3]) + float(usage[4]) )
    
    def getIPAddr(self):
        ips = check_output(['hostname', '--all-ip-addresses'])
        return ips.strip().split(' ')

if __name__ == "__main__":
    myOS = JMOSInfo()

    disk = myOS.getDiskUsage("/") 
    print("\nDisk")
    print(disk)
    print("\nMemory")
    print(myOS.getMemUsage())
    print("\nCPU Info")
    print(myOS.getCPUInfo())
    print("\nCPU Usage")
    print(myOS.getCPUsage())
    print("\nIP Address")
    print(myOS.getIPAddr())
    
    print(disk["total"])
    print( myOS.bytes2Human(disk["total"] * 1024) )
    
