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

class JMRPiSpark:
    __version__ = ""
    Screen = None
    Keyboard = None
    Attitude = None
    Audio = None
    Tone = None

    def __init__(self, version, screen = None, keyboard = None, attitude = None, audio = None, tone = None ):
        """ Init a RPiSpark object instance 
            version -- HW Version (string)
            screen -- OLED / LCD / Other object instance ( None, SSPILScreen or Other )
            keyboard -- Key buttons object instance ( None, SSKeyButtons or Other )
            attitude -- Attitude sensor object instance ( None, MPU6050 or Other )
            audio -- Audio controller object instance ( None, SSAudioDevice or Other )
            tone -- Tone player object instance ( None, JMRPiTonePlayer or Other )
        """

        self.__version__ = version
        self.Screen = screen
        self.Keyboard = keyboard
        self.Attitude = attitude
        self.Audio = audio
        self.Tone = tone
        pass

    def version(self):
        return self.__version__
    pass
