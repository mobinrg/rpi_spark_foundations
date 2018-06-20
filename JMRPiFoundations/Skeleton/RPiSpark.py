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

class RPiSpark:
    __version__ = None
    
    ##
    # \~english
    # A screen object instance, it can be \e SSPILScreen, \e SScreenSSD1306 or other
    # \~chinese
    # 显示屏硬件对象实例，可以是：SSPILScreen，SScreenSSD1306 或其他显示屏硬件对象实例
    #
    # \~
    # @see SSPILScreen
    # @see SScreenSSD1306
    # @see SScreenILI9341
    Screen = None
    
    ##
    # \~english
    # A key buttons object instance, it can be \e RPiKeyButtons or other
    # \~chinese
    # 按键对象实例，可以是： RPiKeyButtons 或其他按键对象实例
    #
    # \~
    # @see RPiKeyButtons
    Keyboard = None

    ##
    # \~english
    # An attitude sensor object instance, it can be \e MPU6050 or other
    # \~chinese
    # 姿态传感器对象实例，可以是： MPU6050 或其他姿态对象实例
    #
    # \~
    # @see MPU6050
    Attitude = None
    
    ##
    # \~english
    # An audio controller object instance, it can be \e RPiAudioDevice or other
    # \~chinese
    # 音频控制对象实例，可以是： RPiAudioDevice 或其他音频控制对象实例
    #
    # \~
    # @see RPiAudioDevice
    Audio = None
    
    ##
    # \~english
    # A tone player object instance, it can be \e RPiTonePlayer or other
    # \~chinese
    # 音符播放对象实例，可以是： RPiTonePlayer 或其他音符播放对象实例
    #
    # \~
    # @see RPiTonePlayer
    Tone = None

    def __init__(self, version, screen = None, keyboard = None, attitude = None, audio = None, tone = None ):
        """!
        \~english
        Init a RPiSpark object instance 
        @param version: Hardware version, (string)
        @param screen: OLED / LCD / Other object instance ( None, SSPILScreen or Other )
        @param keyboard: Key buttons object instance ( None, RPiKeyButtons or Other )
        @param attitude: Attitude sensor object instance ( None, MPU6050 or Other )
        @param audio: Audio controller object instance ( None, RPiAudioDevice or Other )
        @param tone: Tone player object instance ( None, RPiTonePlayer or Other )
        
        \~chinese
        初始化 RPiSpark 对象实例 
        @param version: 硬件版本, (string)
        @param screen: 显示屏对象实例，( 默认： None, 可使用： SSPILScreen 或其他显示屏对象实例 )
        @param keyboard: 按键对象实例 ( 默认： None, 可使用： RPiKeyButtons 或其他按键对象实例 )
        @param attitude: 姿态对象实例 ( 默认： None, 可使用： MPU6050 或其他姿态对象实例 )
        @param audio: 音频控制对象实例 ( 默认： None, 可使用： RPiAudioDevice 或其他音频对象实例 )
        @param tone: 音符播放对象实例 ( 默认： None, 可以使用： RPiTonePlayer 或其他音符播放对象实例 )
        """

        self.__version__ = version
        self.Screen = screen
        self.Keyboard = keyboard
        self.Attitude = attitude
        self.Audio = audio
        self.Tone = tone

    def version(self):
        """!
        \~english
        Get hardware version of RPiSpark
        @return Hardware version
        
        \~chinese
        取得 RPiSpark 硬件版本
        @return 硬件版本
        """
        return self.__version__
