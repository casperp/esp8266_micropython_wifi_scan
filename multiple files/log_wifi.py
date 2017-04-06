""" Test code for future features. This code will log wifi names and type to a
file on the esp or maybe sd card. You can try the code but it is still really early stage.

### test code for class###
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
log = log_wifi.Log_Wifi(wlan.scan())
while True:
	log.log(wlan.scan())
	print(log)
	print(gc.mem_free())
	time.sleep(120)
###__________________###

"""
class Log_Wifi:
    def __init__(self,wifi_list,filename="wifi_list.txt"):
        self.wifi_list = wifi_list
        self.file = filename
        self.list_names = []


    def _write_file(self):
        with open(self.file, 'a') as file:
            for i in self.list_names:
                string = 'Name: '+str(i[0])+'\tsecure: '+str(i[1])+ '\n'
                file.write(string)


    def log(self,wifi_list):
        for i in wifi_list:
            self.list_names.append([str(i[0], 'utf8') ,i[4]])
        self._write_file()

    def __str__(self):
        return ''.join([str(i[0])+'  ' for i in self.list_names])
