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
# Spark Module Base Object
#
# Author: Kunpeng Zhang
# 2018.4.09
#

from time import sleep

class SparkModuleBase:
    _RPiSparkConfig = None
    _RPiSpark = None

    def __init__(self, RPiSparkConfig, RPiSpark):
        self._RPiSparkConfig = RPiSparkConfig
        self._RPiSpark = RPiSpark
        self.setup()

    # Read key button status, return 0 / 1
    def _readKeyButton(self, keyBtn):
        if self._RPiSpark.Keyboard.readKeyButton( keyBtn ) == 0:
            sleep(0.02)
            return 0 if self._RPiSpark.Keyboard.readKeyButton( keyBtn ) else 1
        return 0

    # Read Exit action ( buttn A and Joy UP press down same time )
    def _readExitButtonStatus(self):
        pressA = self._readKeyButton(self._RPiSparkConfig.BUTTON_ACT_A)
        pressUp = self._readKeyButton(self._RPiSparkConfig.BUTTON_JOY_UP)
        return pressA and pressUp
    
    # Read any buttons action ( any action buttns or Joy buttons press down )
    def _readAnyButtonStatus(self):
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_ACT_A): return True
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_ACT_A): return True
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_JOY_UP): return True
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_JOY_DOWN): return True
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_JOY_LEFT): return True
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_JOY_RIGHT): return True
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_JOY_OK): return True

        return False

    def _keyButtonDown(self, channel):
        # example code ... 
        #if channel == self._RPiSparkConfig.BUTTON_ACT_A:
        #    self._actStatus = 2
        #    return
        pass

    def _keyButtonUp(self, channel):
        # example code ... 
        #if channel == self._RPiSparkConfig.BUTTON_ACT_A:
        #    self._actStatus = 2
        #    return
        pass

    # Key button interrupt event callback function
    # Inherit this method to implement your want
    def _callbackKeyButton(self, channel):
        if self._RPiSpark.Keyboard.readKeyButton(channel) == 0:
            self._keyButtonDown(channel)
            return

        if self._RPiSpark.Keyboard.readKeyButton(channel) == 1:
            self._keyButtonUp(channel)
            return

    # Init all key buttons interrupt events or query mode. 
    # Inherit the _keyButtonDown and _keyButtonUp to implement your want
    # mode: Can be { "INT" | "QUERY" }, default is "INT"
    #
    def _initKeyButtons(self, mode = "INT"):
        if mode.upper() == "INT":
            try:
                self._RPiSpark.Keyboard.configKeyButtons(
                    enableButtons = [
                        {"id":self._RPiSparkConfig.BUTTON_ACT_A, "callback":self._callbackKeyButton},
                        {"id":self._RPiSparkConfig.BUTTON_ACT_B, "callback":self._callbackKeyButton},
                        {"id":self._RPiSparkConfig.BUTTON_JOY_UP, "callback":self._callbackKeyButton},
                        {"id":self._RPiSparkConfig.BUTTON_JOY_DOWN, "callback":self._callbackKeyButton},
                        {"id":self._RPiSparkConfig.BUTTON_JOY_LEFT, "callback":self._callbackKeyButton},
                        {"id":self._RPiSparkConfig.BUTTON_JOY_RIGHT, "callback":self._callbackKeyButton},
                        {"id":self._RPiSparkConfig.BUTTON_JOY_OK, "callback":self._callbackKeyButton}
                    ],
                    bounceTime = 10 )
            except:
                pass

        if mode.upper() == "QUERY":
            self._RPiSpark.Keyboard.configKeyButtons([
                {"id":self._RPiSparkConfig.BUTTON_ACT_A, "callback":None},
                {"id":self._RPiSparkConfig.BUTTON_ACT_B, "callback":None},
                {"id":self._RPiSparkConfig.BUTTON_JOY_OK, "callback":None},
                {"id":self._RPiSparkConfig.BUTTON_JOY_UP, "callback":None},
                {"id":self._RPiSparkConfig.BUTTON_JOY_DOWN, "callback":None},
                {"id":self._RPiSparkConfig.BUTTON_JOY_LEFT, "callback":None},
                {"id":self._RPiSparkConfig.BUTTON_JOY_RIGHT, "callback":None}
            ])

    # Release all key button events
    def _releaseKeyButtons(self):
            self._RPiSpark.Keyboard.removeKeyButtonEvent([
                self._RPiSparkConfig.BUTTON_ACT_A,
                self._RPiSparkConfig.BUTTON_ACT_B,
                self._RPiSparkConfig.BUTTON_JOY_UP,
                self._RPiSparkConfig.BUTTON_JOY_DOWN,
                self._RPiSparkConfig.BUTTON_JOY_LEFT,
                self._RPiSparkConfig.BUTTON_JOY_RIGHT,
                self._RPiSparkConfig.BUTTON_JOY_OK
            ])
    
    # note 1-7, None mean is Mute Tone
#     def _beepTone(self, note = None, delay = 0.02, muteDelay = 0.0):
#         if note == None:
#             self._RPiSpark.Tone.playTone(0, 1, delay, muteDelay)
#             return
# 
#         if note>0 and note<=7:
#             try:
#                 tones = [441,495,556,589,661,742,833]
#                 self._RPiSpark.Tone.playTone( tones[note-1], 1, delay, muteDelay )
#                 self._RPiSpark.Tone.stopTone()
#             except:
#                 print("Beep error")
#         
#     def _beep(self):
#         self._beepTone( 2 , 0.01)

    #Subclass inherits initialization work
    #eg: config keyboard, open file, etc.
    #
    def setup(self): raise NotImplementedError

    #Subclass inherits run
    def run(self): raise NotImplementedError
