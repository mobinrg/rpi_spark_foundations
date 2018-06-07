# -*- coding: utf-8 -*-
#
# JMRPi.Spark Provider
#
# Author: Kunpeng Zhang
# 2018.6.7
#
# See LICENSE for details.

def initSpark():
    """
        Create a JMRPiSpark object instance, it contain OLED, Keybuttons, Audio, 
        Speaker, etc. objects instance
        
        return a JMRPiSpark object instance
    """
    from JMRPiFoundations.devices.rpi_devices import HW_CONFIG_RPI_SPARK_Z_1 as HWCONFIG
    from JMRPiFoundations.devices.rpi_spark_z_1_0_0 import JMRPiSparkConfig
    from JMRPiFoundations.skeleton.JMRPiSpark import JMRPiSpark

    from JMRPiDrives.display.JMRPiDisplay_SSD1306 import SSD1306_128x64
    from JMRPiDrives.screen.JMRPiScreen_SSD1306 import SScreenSSD1306
    from JMRPiDrives.key.JMRPiKeyButtons import SSKeyButtons
    from JMRPiDrives.audio.JMRPiAudio import SSAudioDevice

    from JMRPiDrives.attitude.JMRPi_MPU6050 import mpu6050
    from JMRPiDrives.attitude.JMRPi_MPU6050 import DEF_MPU6050_ADDRESS

    #from JMRPiDrives.audio.JMRPiTone import JMRPiTonePlayer

    import spidev
    #open spi bus
    spi = spidev.SpiDev()
    spi.open( JMRPiSparkConfig.DSP_SPI_PORT, JMRPiSparkConfig.DSP_SPI_DEVICE)
    spi.max_speed_hz = JMRPiSparkConfig.DSP_SPI_MAX_SPEED_HZ
    spi.cshigh = False
    spi.mode = 0
    #create display 
    myDisplay = SSD1306_128x64( 
        spi,  
        spiDC = JMRPiSparkConfig.DSP_DC,
        spiReset = JMRPiSparkConfig.DSP_RESET,
        mirrorH = JMRPiSparkConfig.DSP_MIRROR_H, 
        mirrorV = JMRPiSparkConfig.DSP_MIRROR_V
    )
    myDisplay.init()
    myDisplay.on()

    myScreen = SScreenSSD1306( 
        myDisplay, 
        bufferColorMode = JMRPiSparkConfig.SCREEN_BUFFER_COLOR_MODE_BW, 
        displayDirection = JMRPiSparkConfig.SCREEN_ROTATING
    )

    # return JMRPiSpark
    return JMRPiSpark(
            version = HWCONFIG.VERSION,
            screen = myScreen,
            keyboard = SSKeyButtons(),
            attitude = mpu6050( JMRPiSparkConfig.ATTITUDE_SENSOR_ADDR ),
            audio = SSAudioDevice( pinRight = JMRPiSparkConfig.AUDIO_R, pinLeft = JMRPiSparkConfig.AUDIO_L )
#             tone = JMRPiTonePlayer( JMRPiSparkConfig.SPEAKER )
        )
