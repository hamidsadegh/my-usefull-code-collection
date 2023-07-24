from switch import *


def main():
    switch1 = Switch('sw1', '192.168.46.13')
    switch2 = Switch('sw2', '192.168.46.23')
    switch3 = Switch('sw3', '192.168.46.33')

    for switch in Switch.all_switches:
        print(switch.hostname, switch.ip)


if __name__ == '__main__':
    main()
