# -*- coding: utf-8 -*-
#
# RPi.Spark Provider
#
# Author: Kunpeng Zhang
# 2018.6.7
#
# See LICENSE for details.

def initSpark():
    """!
    Create a RPiSpark object instance, it contain OLED, Keybuttons, Audio, 
    Speaker, etc. objects instance

    @return a RPiSpark object instance
    """
    
    #from JMRPiFoundations.Devices.rpi_devices import HW_CONFIG_RPI_SPARK_Z_1 as HWCONFIG
    from JMRPiFoundations.Devices.rpi_spark_z_1_0_0 import RPiSparkConfig
    from JMRPiFoundations.Skeleton.RPiSpark import RPiSpark

    from JMRPiSpark.Drives.Screen.SScreenSSD1306 import SScreenSSD1306
    from JMRPiSpark.Drives.Display.SSD1306 import SSD1306_128x64
    from JMRPiSpark.Drives.Key.RPiKeyButtons import RPiKeyButtons
    from JMRPiSpark.Drives.Audio.RPiAudio import RPiAudioDevice
  
    from JMRPiSpark.Drives.Attitude.MPU6050 import MPU6050
    from JMRPiSpark.Drives.Attitude.MPU6050 import DEF_MPU6050_ADDRESS

    from JMRPiSpark.Drives.Audio.RPiTone import RPiTonePlayer

    import spidev
    #open spi bus
    spi = spidev.SpiDev()
    spi.open( RPiSparkConfig.DSP_SPI_PORT, RPiSparkConfig.DSP_SPI_DEVICE)
    spi.max_speed_hz = RPiSparkConfig.DSP_SPI_MAX_SPEED_HZ
    spi.cshigh = False
    spi.mode = 0
    #create display 
    myDisplay = SSD1306_128x64( 
        spi,  
        spiDC = RPiSparkConfig.DSP_DC,
        spiReset = RPiSparkConfig.DSP_RESET,
        mirrorH = RPiSparkConfig.DSP_MIRROR_H, 
        mirrorV = RPiSparkConfig.DSP_MIRROR_V
    )
    myDisplay.init()
    myDisplay.on()

    myScreen = SScreenSSD1306( 
        myDisplay, 
        bufferColorMode = RPiSparkConfig.SCREEN_BUFFER_COLOR_MODE_BW, 
        displayDirection = RPiSparkConfig.SCREEN_ROTATING
    )

    # return RPiSpark
    return RPiSpark(
            version = RPiSparkConfig.HW_VERSION,
            screen = myScreen,
            keyboard = RPiKeyButtons(),
            attitude = MPU6050( RPiSparkConfig.ATTITUDE_SENSOR_ADDR ),
            audio = RPiAudioDevice( pinRight = RPiSparkConfig.AUDIO_R, pinLeft = RPiSparkConfig.AUDIO_L ),
            tone = RPiTonePlayer( RPiSparkConfig.SPEAKER )
        )