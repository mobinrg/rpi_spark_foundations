RPi Spark Python Foundations
===============================

The Raspberry Pi Spark pHAT board let you to easily develop interesting applications through the GPIO of Raspberry Pi.

Foundations Key Features:

* Device Configs
	-- Hardware config of Spark pHAT

* Skeletons
	-- Some classes for easy and fast development

* Utiles
	-- Some utile classes

* CLI
	-- RPi Spark CLI command line interface: rpi_spark ( 'rpi_spark -h' to show help )
	-- RPi Spark Launcher: rspk ( 'rspk -h' to show help )



Spark pHAT Key Features:

* 128x64 monochrome OLED
* Accelerometers
* Gyroscopes
* Thermometer
* 5-way joystick
* 2 action buttons
* 3.5mm stereo headphone jack
* 1W speaker
* 20 extended GPIO pads

Drives:

* SSD1306 compatible OLED display 
	- Provides screen flipping settings and increase display data transfer rate

* MPU6050 Gyroscopes, Accelerometers and Thermometer Sensors
	- Motion Detection Interrupt, Sleep Mode and independent Trun-ON sensor

* GPIO Buttons
	- Interrupt Support, Polling Support

* Audio
	- Provides audio output switch that can play back OGG, MP3, WAV, etc. music formats via headphones or speakers

* PWM Tone Player
	- PWM generates pitch and plays


Supported:

* Raspberry Pi 2 / 3 / 3+
* Raspberry Pi Zero
* Raspberry Pi Zero W


Requirements:

* Linux
* Python 2.7 or Python 3.x
* JMRPi.Spark Drives Libs 
	-- You need install JMRPi.Spark Drives libs before use this foundsation libs
	-- $ pip install JMRPi.Spark


History:

* v1.0.3	2018.7
* v1.0.0	2018.6	first released


SDK Manual:

* http://doc.mobinrg.com/rpi_spark/sdk/en/


Drive Example:

* http://github.com/mobinrg/rpi_spark_examples
* http://doc.mobinrg.com/download/rpi_spark/spark_examples.zip


Written by Kunpeng Zhang.
MIT license, all text above must be included in any redistribution




=======================
 Chinese ( Simplified )
=======================
树梅派 ZERO Spark 火花扩展板 Python 开发框架

我们设计的树梅派火花扩展板让您更轻松的通过树梅派 GPIO 开发有趣的应用。

开发框架:

* 设备配置
	-- 火花扩展板参数配置
	
* 应用架构
	-- 让火花扩展板开发更简洁且快速的基础类库
	
* 效用类
	-- 有用的类库


火花扩展板设计包含:

* 显示屏: 128x64 单色 OLED
* 陀螺仪
* 加速计
* 温度计
* 5方向游戏按键
* 2个动作按键
* 3.5mm 立体声耳机插座
* 1W 扬声器
* 20 个扩展 GPIO 焊盘


包含的驱动：

* SSD1306 兼容的 OLED 显示屏
	-- 提供屏幕翻转设定，提高显示数据传输速率

* MPU6050 陀螺仪，加速计，温度计传感器
	-- 运动检测中断，睡眠模式，独立的传感器开启

* GPIO 按键				
	-- 中断支持，轮询支持

* 音频
	-- 提供音频输出开关，能够通过耳机或扬声器回放 OGG, MP3， WAV，等音乐格式

* PWM 音调
	-- PWM 生成音调并且播放

* CLI
	-- RPi Spark CLI command line interface: rpi_spark ( 'rpi_spark -h' to show help )
	-- RPi Spark Launcher: rspk ( 'rspk -h' to show help )

支持的树梅派：

* Raspberry Pi 2 / 3 / 3+
* Raspberry Pi Zero
* Raspberry Pi Zero W


系统要求:

* Linux
* Python 2.7 or Python 3.x
* JMRPi.Spark Drives Libs 
	-- 在使用此基础库之前, 您需要安装 JMRi.Spark 驱动库
	-- $ pip install JMRPi.Spark

版本历史:

* v1.0.3	2018.7
* v1.0.0	2018.6	第一次发布


SDK 参考:

* http://doc.mobinrg.com/rpi_spark/sdk/en/
* http://doc.mobinrg.com/rpi_spark/sdk/zh_CN/


驱动示例代码:

* http://github.com/mobinrg/rpi_spark_examples
* http://doc.mobinrg.com/download/rpi_spark/spark_examples.zip

由 Kunpeng Zhang 撰写。
MIT许可证，上述所有文本必须包含在任何重新发布中




=======================
 Chinese ( Traditional )
=======================
樹梅派 ZERO Spark 火花擴展板 Python 開發架構

我們設計的樹梅派火花擴展板讓您更輕鬆的通過樹梅派 GPIO 開發有趣的應用。


開發框架:

* 設備配置
	-- 火花擴展板參數配置

* 應用架構
	-- 讓火花擴展板開發更簡潔且快速的基礎類庫

* 效用類
	-- 有用的類庫
	
* CLI
	-- RPi Spark CLI command line interface: rpi_spark ( 'rpi_spark -h' to show help )
	-- RPi Spark Launcher: rspk ( 'rspk -h' to show help )


火花擴展板設計包含:

* 顯示屏: 128x64 單色 OLED
* 陀螺儀
* 加速計
* 溫度計
* 5方向遊戲按鍵
* 2個動作按鍵
* 3.5mm 立體聲耳機插座
* 1W 揚聲器
* 20 個擴展 GPIO 焊盤


包含的驅動：

* SSD1306 兼容的 OLED 顯示屏
	-- 提供屏幕翻轉設定，提高顯示數據傳輸速率

* MPU6050 陀螺儀，加速計，溫度計傳感器
	-- 運動檢測中斷，睡眠模式，獨立的傳感器開啟

* GPIO 按鍵
	-- 中斷支持，輪詢支持

* 音頻
	-- 提供音頻輸出開關，能夠通過耳機或揚聲器回放 OGG, MP3， WAV，等音樂格式

* PWM 音調
	-- PWM 生成音調並且播放


支持的樹梅派：

* Raspberry Pi 2 / 3 / 3+
* Raspberry Pi Zero
* Raspberry Pi Zero W


版本歷史:
* v1.0.3	2018.7
* v1.0.0	2018.6 第一次發布


系統需求:

* Linux
* Python 2.7 or Python 3.x
* JMRPi.Spark Drives Libs
	-- 在使用此基礎庫之前, 您需要安裝 JMRi.Spark 驅動庫
	-- $ pip install JMRPi.Spark


SDK 参考:

* http://doc.mobinrg.com/rpi_spark/sdk/en/
* http://doc.mobinrg.com/rpi_spark/sdk/zh_CN/


驅動示例源碼:

* http://github.com/mobinrg/rpi_spark_examples
* http://doc.mobinrg.com/download/rpi_spark/spark_examples.zip


由 Kunpeng Zhang 撰寫。
MIT許可證，上述所有文本必須包含在任何重新發布中
