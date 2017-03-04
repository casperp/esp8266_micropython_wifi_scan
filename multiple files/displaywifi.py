import network
import machine
import ssd1306
import utime


class DisplayWifi:
    def __init__(self,pin1='5',pin2='4'):
        self.pin1 = pin1
        self.pin2 = pin2
        self.name = ''
        self.strengt = ''
        self.status = ''
        self.kanaal = ''
    	self.i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
    	self.oled = ssd1306.SSD1306_I2C(128, 64, self.i2c)
    	self.oled.fill(1)
    	self.oled.show()
    	self.wlan = network.WLAN(network.STA_IF)
    	self.wlan.active(True)

    def format(self):
        try:
            wlan_list = self.wlan.scan()
        except:
    		wlan_list = [['NONE','NONE','NONE','NONE','NONE','NONE']]
        for i in wlan_list:
            self.name = str(i[0], 'utf8')
            self.strengt = str(i[3]) + ' dBm'
            self.kanaal = 'Channel: ' + str(i[2])
            self.status = self.get_secure(i[4])
            self.show_display()

    def get_secure(self, num):
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

    def show_display(self):
        self.oled.fill(0)
        self.oled.show()
        if len(self.name) > 15:
            self.oled.text(self.name[0:15],0,0)
            self.oled.text(self.name[15:int(len(self.name))],0,10)
        else:
            self.oled.text(self.name,0,0)
        self.oled.text(self.strengt,30,20)
        self.oled.text(self.status,30,30)
        self.oled.text(self.kanaal, 30,40)
        self.oled.show()
        utime.sleep_ms(10000)

    def __str__(self):
        return "Name: {}.\n{}\n{}.\n{}.".format(self.name, self.strengt, self.kanaal, self.status)
