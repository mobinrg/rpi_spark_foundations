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
# See LICENSE.rst for details.

import subprocess
import re

class OSInfo:

    def _cmd(self, cmdParams):
        cmd = subprocess.Popen( cmdParams, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        out,error = cmd.communicate() 
        return out.splitlines()

    def bytesUnit2HM(self, n):
        """!
            bytes2Unit(10000) => '9K'
            bytes2Unit(100001221) => '95M'
        """

        unitSymbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
        pfix = {}
        for i, s in enumerate(unitSymbols):
            pfix[s] = 1 << (i + 1) * 10

        for s in reversed(unitSymbols):
            if n >= pfix[s]:
                val = int(float(n) / pfix[s])
                return '%s%s' % (val, s)

        return "%sB" % n

    def getMemUsage(self):
        memory = self._cmd(['free'])

        cols = re.sub(r"(( )+|(\n)+)", " ", str(memory[1]))
        cols = re.sub(r'((b\')|(\\t)|(\'))', "", str(cols))
        cols = re.sub("(.*\:)", "", str(cols))
        cols = re.sub("\A\s+", "", str(cols))
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
    
        cols = re.sub(r'(( )+|(\n)+)', " ", str(disk[1]))
        cols = re.sub(r'((b\')|(\\t)|(\'))', "", str(cols))
        cols = re.sub("(.*\:)", "", str(cols))
        cols = re.sub("\A\s+", "", str(cols))
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
            item = re.sub(r'((\t)+|(\n)+)', "", str(i))
            item = re.sub(r'((b\')|(\\t)|(\'))', "", str(item))
            info = item.split(': ')
            try:
                if info[0] != "processor": result[info[0].replace(" ", "_").lower()] = info[1]
            except:
                continue
        return result

    def getCPUsage(self):
        """!
            https://github.com/Leo-G/DevopsWiki/wiki/How-Linux-CPU-Usage-Time-and-Percentage-is-calculated
            <pre>
             cat /proc/stat
                 user nice system idle iowait  irq  softirq steal guest guest_nice
            cpu  4705 356  584    3699   23    23     0       0     0          0
            </pre>

            Formula
            To calculate Linux CPU usage time subtract the idle CPU time from the total CPU time as follows:
            Total_CPU_time_since_boot(TC_TSB) = user + nice + system + idle + iowait + irq + softirq + steal
            Total_CPU_Idle_time_since_boot(TCI_TSB) = idle + iowait
            Total_CPU_usage_time_since_boot(TCU_TSB) = Total_CPU_time_since_boot - Total_CPU_Idle_time_since_boot
            Total_CPU_percentage(TCP) = Total_CPU_usage_time_since_boot / Total_CPU_time_since_boot * 100
        """
        cpu = self._cmd(["grep", "cpu", "/proc/stat" ])
        cols = re.sub(r'(( )+|(\n)+)', " ", str(cpu[0]))
        cols = re.sub(r'((b\')|(\\t)|(\'))', "", str(cols))
        cols = re.sub(r"\A\s+", "", str(cols))
        usage = cols.split(' ')
        #print(usage)

        TC_TSB = 0.00
        for i in range(1,9):
            TC_TSB += float(usage[i])

        TCI_TSB = float(usage[4]) + float(usage[5])
        TCU_TSB = TC_TSB - TCI_TSB
        TCP = TCU_TSB / TC_TSB

        #print(TC_TSB, TCI_TSB, TCU_TSB, TCP)
        #print(float(1.00)/TCI_TSB)
        #return ( float(usage[1]) + float(usage[3]) ) / ( float(usage[1]) + float(usage[3]) + float(usage[4]) )
        return TCP

    def getIPAddr(self):
        ips = self._cmd(['hostname', '--all-ip-addresses'])
        cols = re.sub(r"(( )+|(\n)+)", " ", str(ips[0]))
        cols = re.sub("\A\s+", "", str(cols))
        cols = re.sub("((b')|( ')+)", "", str(cols))
        return cols.strip().split(' ')


if __name__ == "__main__":
    myOS = OSInfo()

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
    print( myOS.bytesUnit2HM(disk["total"] * 1024) )