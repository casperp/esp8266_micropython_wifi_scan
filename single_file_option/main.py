import webrepl
import network
import machine
import ssd1306
import utime
import ubinascii
import math
webrepl.start()
"""default connection:
esp8266 -> OLED display
5(d1)   ->  scl
6(d2)   ->  sda
GND     ->  GND
3.3v    ->  vcc"""


def return_wifi_sec(num):
	try:
		if int(num) == 0:
			return 'Open wifi'
		elif int(num) == 1:
			return 'WEP'
		elif int(num) ==2:
			return 'WPA-PSK'
		elif int(num) == 3:
			return 'WPA2-PSK'
		elif int(num) == 4:
			return 'WPA/WPA2-PSK'
		else:
			return str(num)
	except:
		return num


def main():
	i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
	oled = ssd1306.SSD1306_I2C(128, 64, i2c)
	oled.fill(1)
	oled.show()
	wlan = network.WLAN(network.STA_IF)
	wlan.active(True)
	while True:
		try:
			wlan_list = wlan.scan()
		except:
			wlan_list = [['NONE','NONE','NONE','NONE','NONE','NONE']]
		for i in wlan_list:
			name = str(i[0], 'utf8')
			var = str(i[3])+' dBm'
			status = return_wifi_sec(i[4])
			kanaal = 'channel ' + str(i[2])
			oled.fill(0)
	   		oled.show()
			if len(name) > 15:
				oled.text(name[0:15],0,0)
				oled.text(name[15:int(len(name))],0,10)
			else:
				oled.text(name,0,0)
			oled.text(var,30,20)
			oled.text(status,30,30)
			oled.text(kanaal, 30,40)
			oled.show()
			utime.sleep_ms(10000)
main()
