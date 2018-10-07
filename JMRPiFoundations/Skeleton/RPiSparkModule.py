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
import RPi.GPIO as GPIO

class RPiSparkModule:
    """!
    \~english
    RPiSparkModule is a basic class designed for fast and easy development 
    of RPi-Spark pHAT applications. It contains the required input and 
    output object instances and some common processing functions. 
    Just simply inherit and implement the setup() and run() functions 
    to fast and easily create interesting RPi-Spark pHAT applications

    \~chinese
    RPiSparkModule 是为快速且更容易的开发 RPi-Spark pHAT 应用而设计的基础类，
    它包含了所需的输入和输出对象实例和一些常用的处理函数功能。仅需继承并且实现 
    setup() 和 run() 两个函数即可快速容易的创建丰富有趣的 RPi-Spark pHAT 应用
    """

    ###
    # a RPiSparkConfig instance
    # @see RPiSparkConfig
    RPiSparkConfig = None

    ###
    # a RPiSpark instance
    # @see RPiSpark
    RPiSpark = None

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
        self.RPiSparkConfig = RPiSparkConfig
        self.RPiSpark = RPiSpark
        self.setup()

    def readKeyButton(self, keyBtn):
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
        if self.RPiSpark.Keyboard.readKeyButton( keyBtn ) == 0:
            sleep(0.015)
            return True if self.RPiSpark.Keyboard.readKeyButton( keyBtn ) == 0 else False
        return False

    def readExitButtonStatus(self):
        """!
        \~english
        Read Exit action ( button A and Joy UP press down same time )
        @return boolean
            @retval True: Exit key buttons did pressed
            @retval False: Exit key buttons didn't press
            
        \~chinese
        查询退出组合按键状态 ( button A 和 Joy UP 同时按下 )
        @return boolean
            @retval True: 退出键被按下
            @retval False: 未按退出键
        """
        pressA = self.readKeyButton(self.RPiSparkConfig.BUTTON_ACT_A)
        pressUp = self.readKeyButton(self.RPiSparkConfig.BUTTON_JOY_UP)
        return pressA and pressUp

    def readAnyButtonStatus(self):
        """!
        \~english
        Read any buttons action ( any action buttons or Joy buttons had press down )
        @return int( > 0 ) or boolean
            @retval int: Key button had pressed and this value is key button io number
            @retval False: Not key button press

        \~chinese
        检查任意按键是否按下（ 包括动作按键和游戏方向按键 ）
        @return 整数 > 0 或 布尔值
            @retval 整数: 有按键按下，返回值即为按键 ID
            @retval False: 没有按键按下
        """
        if self.readKeyButton(self.RPiSparkConfig.BUTTON_ACT_A):
            return self.RPiSparkConfig.BUTTON_ACT_A
        if self.readKeyButton(self.RPiSparkConfig.BUTTON_ACT_B):
            return self.RPiSparkConfig.BUTTON_ACT_B
        if self.readKeyButton(self.RPiSparkConfig.BUTTON_JOY_UP):
            return self.RPiSparkConfig.BUTTON_JOY_UP
        if self.readKeyButton(self.RPiSparkConfig.BUTTON_JOY_DOWN):
            return self.RPiSparkConfig.BUTTON_JOY_DOWN
        if self.readKeyButton(self.RPiSparkConfig.BUTTON_JOY_LEFT):
            return self.RPiSparkConfig.BUTTON_JOY_LEFT
        if self.readKeyButton(self.RPiSparkConfig.BUTTON_JOY_RIGHT):
            return self.RPiSparkConfig.BUTTON_JOY_RIGHT
        if self.readKeyButton(self.RPiSparkConfig.BUTTON_JOY_OK):
            return self.RPiSparkConfig.BUTTON_JOY_OK

        return False

    def onKeyButtonDown(self, channel):
        """!
        \~english
        Key button down event, inherited and processed
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
        def onKeyButtonDown(self, channel):
            if channel == self.RPiSparkConfig.BUTTON_ACT_A:
               self._actStatus = 2
               return \n
            if channel == self.RPiSparkConfig.BUTTON_ACT_B:
               self._actStatus = 3
               return
        </pre>
        """
        pass

    def onKeyButtonUp(self, channel):
        """!
        \~english
        Key button release event, inherited and processed
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
        def onKeyButtonUp(self, channel):
            if channel == self.RPiSparkConfig.BUTTON_ACT_A:
               self._actStatus = 2
               return \n
            if channel == self.RPiSparkConfig.BUTTON_ACT_B:
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
        RPiSparkModule#onKeyButtonDown and 
        RPiSparkModule#onKeyButtonUp to implement your want

        \~chinese
        按键中断事件回调功能。
        @note 基本处理已经实现，不建议继承并重写该方法。 
        请继承 RPiSparkModule#onKeyButtonDown 和 RPiSparkModule#onKeyButtonUp 
        实现你想要处理的按键操作
        """
        if self.RPiSpark.Keyboard.readKeyButton(channel) == 0:
            self.onKeyButtonDown(channel)
            return

        if self.RPiSpark.Keyboard.readKeyButton(channel) == 1:
            self.onKeyButtonUp(channel)
            return

    def initKeyButtons(self, mode = "INT"):
        """!
        \~english
        Initialize all key buttons interrupt events or query mode. 
        Inherit the onKeyButtonDown and onKeyButtonUp to implement your want
        @param mode: key button init mode, it can be: { "INT" | "QUERY" }, default is "INT"
        
        \~chinese
        初始化全部按键，可以设定为中断模式或查询模式
        子类继承 onKeyButtonDown 和 onKeyButtonUp 实现按键中断模式下的操作
        @param mode: 按键模式, 取值： "INT" 或 "QUERY", 默认： "INT"
        """
        if mode.upper() == "INT":
            try:
                self.RPiSpark.Keyboard.configKeyButtons(
                    enableButtons = [
                        {"id":self.RPiSparkConfig.BUTTON_ACT_A, "callback":self._callbackKeyButton},
                        {"id":self.RPiSparkConfig.BUTTON_ACT_B, "callback":self._callbackKeyButton},
                        {"id":self.RPiSparkConfig.BUTTON_JOY_UP, "callback":self._callbackKeyButton},
                        {"id":self.RPiSparkConfig.BUTTON_JOY_DOWN, "callback":self._callbackKeyButton},
                        {"id":self.RPiSparkConfig.BUTTON_JOY_LEFT, "callback":self._callbackKeyButton},
                        {"id":self.RPiSparkConfig.BUTTON_JOY_RIGHT, "callback":self._callbackKeyButton},
                        {"id":self.RPiSparkConfig.BUTTON_JOY_OK, "callback":self._callbackKeyButton}
                    ],
                    bounceTime = 10 )
            except:
                pass

        if mode.upper() == "QUERY":
            self.RPiSpark.Keyboard.configKeyButtons([
                {"id":self.RPiSparkConfig.BUTTON_ACT_A, "callback":None},
                {"id":self.RPiSparkConfig.BUTTON_ACT_B, "callback":None},
                {"id":self.RPiSparkConfig.BUTTON_JOY_OK, "callback":None},
                {"id":self.RPiSparkConfig.BUTTON_JOY_UP, "callback":None},
                {"id":self.RPiSparkConfig.BUTTON_JOY_DOWN, "callback":None},
                {"id":self.RPiSparkConfig.BUTTON_JOY_LEFT, "callback":None},
                {"id":self.RPiSparkConfig.BUTTON_JOY_RIGHT, "callback":None}
            ])

    def releaseKeyButtons(self):
        """!
        \~english
        Release all events of key buttons

        \~chinese
        释放全部按键事件回调
        """
        self.RPiSpark.Keyboard.removeKeyButtonEvent([
            self.RPiSparkConfig.BUTTON_ACT_A,
            self.RPiSparkConfig.BUTTON_ACT_B,
            self.RPiSparkConfig.BUTTON_JOY_UP,
            self.RPiSparkConfig.BUTTON_JOY_DOWN,
            self.RPiSparkConfig.BUTTON_JOY_LEFT,
            self.RPiSparkConfig.BUTTON_JOY_RIGHT,
            self.RPiSparkConfig.BUTTON_JOY_OK
        ])

    def onDeviceShake(self, channel):
        """
        \~english
        Device shake detect event
        @attention * Do not do time-consuming operations in this function

        Example:
        
        \~chinese
        设备摇晃检测事件
        @attention * 不要在此函数中做耗时的操作

        示例代码：

        \~
        <pre>
        def onDeviceShake(self, channel):
            self._shakeCount += 1
            print("\n--- SHAKED DEVICE: {} ---\n".format(self._shakeCount))
        </pre>
        """
        pass

    def enableShakeDetect(self):
        """
        \~english
        Enable device shake detect

        @return Boolean
            True: shake detect enabled
            False: shake detect false

        \~chinese
        开启设备摇晃检测

        @return Boolean
            True：摇晃检测开启成功
            False：摇晃检测开启失败
        """
        if self.RPiSpark.Attitude != None:
            # Init shake check INT -- default GPIO 25 ( BCM )
            GPIO.setup( self.RPiSparkConfig.ATTITUDE_INT, GPIO.IN, pull_up_down=GPIO.PUD_UP )
            GPIO.add_event_detect( self.RPiSparkConfig.ATTITUDE_INT, GPIO.RISING, callback=self.onDeviceShake, bouncetime=20 )
            # enable motion check int
            self.RPiSpark.Attitude.setMotionInt()
            return True
        else:
            return False

    def disableShakeDetect(self):
        """
        \~english
        Disabled device shake detect
        
        @return Boolean
            True: shake detect disabled
            False: shake detect can not disable or failed

        \~chinese
        关闭设备摇晃检测
        
        @return Boolean
            True：摇晃检测关闭成功
            False：摇晃检测关闭失败
        """
        if self.RPiSpark.Attitude != None:
            # remove attitude int event
            GPIO.remove_event_detect( self.RPiSparkConfig.ATTITUDE_INT )
            # disabled motion check int
            self.RPiSpark.Attitude.disableInt()
            return True
        else:
            return False

    def beepTone(self, note = None, delay = 0.02, muteDelay = 0.05, tonePlayer = None):
        """!
        \~english
        Play an beep tone
        @param note: a note, can be chosen: 1 ~ 7.
        @param delay: note delay time, unit: second
        @param mutedDelay: muted time after playing, unit: second
        @param tonePlayer: a RPiTonePlayer object instance, 
                if None means use self.RPiSpark.Tone to play a note.

        \~chinese
        播放嘟嘟声
        @param note: 音符, 取值： 1 到 7
        @param delay: 音符播放时间, 单位: 秒
        @param mutedDelay: 音符播放后禁音时间, 单位： 秒
        @param tonePlayer: RPiTonePlayer 音符播放器对象实例，
                如果是 None 使用模块内置对象 self.RPiSpark.Tone 播放。
        """

        if tonePlayer != None:
            myTone = tonePlayer
        elif self.RPiSpark.Tone != None:
            myTone = self.RPiSpark.Tone

        if myTone == None: return
        if note == None:
            myTone.stopTone()
            return

        if note>0 and note<=7:
            try:
                tones = [ 441,495,556,589,661,742,833 ]
                myTone.playTone( tones[note-1], 1, delay, muteDelay )
                myTone.stopTone()
            except:
                print("Beep error")

    def beep(self, tonePlayer = None):
        self.beepTone( note = 3 , delay = 0.02, muteDelay = 0.02, tonePlayer = tonePlayer )

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
