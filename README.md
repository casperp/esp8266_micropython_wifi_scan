# esp8266_micropython_wifi_scan
Shows wifi scan on ssd1306 OLED display.

###Requirements:
  1.[MicroPython driver for SSD1306 OLED displays from Adafruit.](https://github.com/adafruit/micropython-adafruit-ssd1306)

  2.MicroPython v1.8.6-7

###Features:
  1. ssid
  2. RSSI
  3. Channel
  4. Security

###How to use and install.

There are two ways to run the script on the esp8266.
  First upload the script, There are two options for this
    1. upload with [webrepl](http://micropython.org/webrepl/?)
    2. upload with [ampy by adafruit](https://github.com/adafruit/ampy).

For the single file version you need the upload the <i>single_file/main.py</i> and [SSD1306.py](https://github.com/adafruit/micropython-adafruit-ssd1306/blob/master/ssd1306.py)
    if you don't already have done this. After uploading replug the board intro the
    power source or use the restart button. Now the display should go white and then show the WIFI information.

For the Multiple file's option you need to upload <i>Multiple files/displaywifi.py</i> and <i>Multiple files/main.py
</i> also [SSD1306.py](https://github.com/adafruit/micropython-adafruit-ssd1306/blob/master/ssd1306.py)
  is needed. After uploading replug the board intro the power source or use the restart button.
  Now the display should go white and then show the WIFI information.
