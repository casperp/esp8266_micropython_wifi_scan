import webrepl
import network
import displaywifi
webrepl.start()
"""" import network,displaywifi module and webrepl for http://micropython.org/webrepl/?
default connection:
esp8266 -> OLED display
5(d1)   ->  scl
6(d2)   ->  sda
GND     ->  GND
3.3v    ->  VCC"""



def main():
    display = displaywifi.DisplayWifi(5,4)
    # use the displaywifi on the pins 4,5
    while True:
        display.format()
        print(display)
        # print the information thatś shown on the screen.
main()
