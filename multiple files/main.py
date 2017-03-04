import webrepl
import network
import displaywifi
webrepl.start()
"default pins 5, 4 "


def main():
    display = displaywifi.DisplayWifi(5,4)
    while True:
        display.format()
        print(display)
main()
