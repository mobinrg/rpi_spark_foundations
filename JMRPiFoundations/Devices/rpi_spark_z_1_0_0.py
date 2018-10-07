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
# RPi-Spark Device Config
# 树梅火花 -- 配置文件
#
# Author: Kunpeng Zhang
# 2018.3.20
#
# Supported Hardware ( 支持硬件 )
# v0.0.x
# v1.0.x
# v1.1.0
#

class RPiSparkConfig:
    # #######################################################################
    # Hardware version

    HW_VERSION      = "RPi_SPARK_Z_1.0.0"

    # #######################################################################
    # Display PINs  SPI_0
    # SSD1306 OLED 128x64

    DSP_RESET       = None
    DSP_DC          = 9  #use MISO for DC
    DSP_SPI_PORT    = 0
    DSP_SPI_DEVICE  = 0
    DSP_SPI_MAX_SPEED_HZ = 6000000  #up to 8500000

    #Display mirror
    DSP_MIRROR_H    = True
    DSP_MIRROR_V    = True

    # Screen rotating, can be chosen in [ 0, 90, 180, 270 ]
    SCREEN_ROTATING = 0
    # Screen buffer color mode, can be chosen in [ "1", "RGB" ]
    SCREEN_BUFFER_COLOR_MODE_RGB = "RGB"
    SCREEN_BUFFER_COLOR_MODE_BW = "1"

    # I2C Bus id
    I2C_BUS_PORT    = 1
    # Attitude sensor -- Accel/Gyro/Temp MPU6050 I2C
    ATTITUDE_SENSOR_ADDR = 0x68
    ATTITUDE_INT    = 25

    # #######################################################################
    # Keyboard include Joystick buttons and Action buttons, 
    # keyboard use BCM mode, there are keyboard layout:
    # 
    #             [JOY UP]                                    [ACT_Y]
    # [JOY LEFT]              [JOY RIGHT]             [ACT_A]         [ACT_B]
    #             [JOY DOWN]                                  [ACT_X]
    #
    # Action Buttons    BCM_IO_NUM

    BUTTON_ACT_A        = 22
    BUTTON_ACT_B        = 23
    # BUTTON_ACT_X        = None
    # BUTTON_ACT_Y        = None
 
    # Joy Buttons       BCM_IO_NUM
    BUTTON_JOY_LEFT     = 26
    BUTTON_JOY_RIGHT    = 27
    BUTTON_JOY_UP       = 5
    BUTTON_JOY_DOWN     = 6
    BUTTON_JOY_OK       = 24
 
    # #######################################################################
    # Audio PINs
    # PWM - Audio
    # GPIO12 - set mode ALT0
    # GPIO13 - set mode ALT0

    AUDIO_L = 12
    AUDIO_R = 13
    SPEAKER = 12

    # #######################################################################
    # Available IOs
    # Physical numbers and BCM Number

    PHY_IO_AVAILABLE = [7,8,10,11,12,26,27,28,35,36,38,40]
    BCM_IO_AVAILABLE = [4,14,15,17,18,7,0,1,19,16,20,21]
