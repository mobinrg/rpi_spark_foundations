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

class RPiSparkModule:
    """!
    \~english
    RPiSparkModule is a basic class designed for fast and easy development 
    of RPi Spark Shield applications. It contains the required input and 
    output object instances and some common processing functions. 
    Just simply inherit and implement the setup() and run() functions 
    to fast and easily create interesting RPi Spark Shield applications

    \~chinese
    RPiSparkModule 是为快速且更容易的开发 RPi Spark Shield 应用而设计的基础类，
    它包含了所需的输入和输出对象实例和一些常用的处理函数功能。仅需继承并且实现 
    setup() 和 run() 两个函数即可快速容易的创建丰富有趣的 RPi Spark Shield 应用
    """

    _RPiSparkConfig = None
    _RPiSpark = None

    def __init__(self, RPiSparkConfig, RPiSpark):
        """!
        \~english
        Initialize the RPiSparkModule object instance
        @param RPiSparkConfig: a RPiSparkConfig instance
        @param RPiSpark: a RPiSpark instance
        
        \~chinese
        初始化 RPiSparkModule 对象实例
        @param RPiSparkConfig: RPiSparkConfig 对象实例
        @param RPiSpark: RPiSpark 对象实例
        """
        self._RPiSparkConfig = RPiSparkConfig
        self._RPiSpark = RPiSpark
        self.setup()

    def _readKeyButton(self, keyBtn):
        """!
        \~english
        Read key button status
        @param keyBtn: io number of key button
        @return boolean
            @retval True: Key buttons did pressed
            @retval False: Key buttons didn't press

        \~chinese
        读取按键 IO 状态
        @param keyBtn: 按键 IO 编号
        @return 布尔值
            @retval True: 按键按下
            @retval False: 按键未操作
        """
        if self._RPiSpark.Keyboard.readKeyButton( keyBtn ) == 0:
            sleep(0.015)
            return True if self._RPiSpark.Keyboard.readKeyButton( keyBtn ) == 0 else False
        return False

    def _readExitButtonStatus(self):
        """!
        \~english
        Read Exit action ( buttn A and Joy UP press down same time )
        @return boolean
            @retval True: Exit key buttons did pressed
            @retval False: Exit key buttons didn't press
            
        \~chinese
        查询退出组合按键状态 ( buttn A 和 Joy UP 同时按下 )
        @return boolean
            @retval True: 退出键被按下
            @retval False: 未按退出键
        """
        pressA = self._readKeyButton(self._RPiSparkConfig.BUTTON_ACT_A)
        pressUp = self._readKeyButton(self._RPiSparkConfig.BUTTON_JOY_UP)
        return pressA and pressUp

    def _readAnyButtonStatus(self):
        """!
        \~english
        Read any buttons action ( any action buttns or Joy buttons had press down )
        @return int( > 0 ) or boolean
            @retval int: Key button had pressed and this value is key button io number
            @retval False: Not key button press

        \~chinese
        检查任意按键是否按下（ 包括动作按键和游戏方向按键 ）
        @return 整数 > 0 或 布尔值
            @retval 整数: 有按键按下，返回值即为按键 ID
            @retval False: 没有按键按下
        """
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_ACT_A):
            return self._RPiSparkConfig.BUTTON_ACT_A
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_ACT_B):
            return self._RPiSparkConfig.BUTTON_ACT_B
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_JOY_UP):
            return self._RPiSparkConfig.BUTTON_JOY_UP
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_JOY_DOWN):
            return self._RPiSparkConfig.BUTTON_JOY_DOWN
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_JOY_LEFT):
            return self._RPiSparkConfig.BUTTON_JOY_LEFT
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_JOY_RIGHT):
            return self._RPiSparkConfig.BUTTON_JOY_RIGHT
        if self._readKeyButton(self._RPiSparkConfig.BUTTON_JOY_OK):
            return self._RPiSparkConfig.BUTTON_JOY_OK

        return False

    def _keyButtonDown(self, channel):
        """!
        \~english
        Key down event, inherited and processed
        @param channel: key button ID
        @attention * Do not do time-consuming operations in this function

        Example:

        \~chinese
        按键按下事件，继承并对按键进行处理。
        @param channel: 按键 ID
        @attention * 不要在此函数中做耗时的操作

        示例代码：

        \~
        <pre>
        def _keyButtonDown(self, channel):
            if channel == self._RPiSparkConfig.BUTTON_ACT_A:
               self._actStatus = 2
               return \n
            if channel == self._RPiSparkConfig.BUTTON_ACT_B:
               self._actStatus = 3
               return
        </pre>
        """
        pass

    def _keyButtonUp(self, channel):
        """!
        \~english
        Key release event, inherited and processed
        @param channel: key button ID
        @attention * Do not do time-consuming operations in this function

        Example:
        
        \~chinese
        按键释放事件，继承并对按键进行处理。
        @param channel: 按键 ID
        @attention * 不要在此函数中做耗时的操作

        示例代码：

        \~
        <pre>
        def _keyButtonUp(self, channel):
            if channel == self._RPiSparkConfig.BUTTON_ACT_A:
               self._actStatus = 2
               return \n
            if channel == self._RPiSparkConfig.BUTTON_ACT_B:
               self._actStatus = 3
               return
        </pre>
        """
        pass

    def _callbackKeyButton(self, channel):
        """!
        \~english
        Key buttons interrupt event callback function.
        @note Basic processing has been implemented and it is not recommended to 
        inherit and rewrite this method. Please inherit the 
        RPiSparkModule#_keyButtonDown and 
        RPiSparkModule#_keyButtonUp to implement your want
        
        \~chinese
        按键中断事件回调功能。
        @note 基本处理已经实现，不建议继承并重写该方法。 
        请继承 RPiSparkModule#_keyButtonDown 和 RPiSparkModule#_keyButtonUp 
        实现你想要处理的按键操作
        """
        if self._RPiSpark.Keyboard.readKeyButton(channel) == 0:
            self._keyButtonDown(channel)
            return

        if self._RPiSpark.Keyboard.readKeyButton(channel) == 1:
            self._keyButtonUp(channel)
            return

    def _initKeyButtons(self, mode = "INT"):
        """!
        \~english
        Initialize all key buttons interrupt events or query mode. 
        Inherit the _keyButtonDown and _keyButtonUp to implement your want
        @param mode: key button init mode, it can be: { "INT" | "QUERY" }, default is "INT"
        
        \~chinese
        初始化全部按键，可以设定为中断模式或查询模式
        子类继承 _keyButtonDown 和 _keyButtonUp 实现按键中断模式下的操作
        @param mode: 按键模式, 取值： "INT" 或 "QUERY", 默认： "INT"
        """
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

    def _releaseKeyButtons(self):
        """!
        \~english
        Release all events of key buttons

        \~chinese
        释放全部按键事件回调
        """
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
    def _beepTone(self, note = None, delay = 0.02, muteDelay = 0.05):
        if note == None:
            self._RPiSpark.Tone.stopTone()
            # self._RPiSpark.Tone.playTone( freq=note, reps=1, delay=delay, muteDelay=muteDelay )
            return
 
        if note>0 and note<=7:
            try:
                tones = [ 441,495,556,589,661,742,833 ]
                self._RPiSpark.Tone.playTone( tones[note-1], 1, delay, muteDelay )
                self._RPiSpark.Tone.stopTone()
            except:
                print("Beep error")

    def _beep(self):
        self._beepTone( note = 3 , delay = 0.02, muteDelay = 0.02 )

    def setup(self):
        """!
        \~english
        Subclass inherits and implements initialization work
        eg: config keyboard, open file, etc.

        \~chinese
        子类继承并实现初始化一些工作
        例如：配置键盘，打开文件，读取资源，等 ...
        """
        raise NotImplementedError

    def run(self):
        """!
        \~english
        Subclasses inherits and implements application
        \~chinese
        子类继承并实现应用
        """
        raise NotImplementedError
