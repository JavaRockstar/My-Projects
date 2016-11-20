#!/usr/bin/env python3

while True:
    import os
    import sys

    class color:
        CYAN = '\033[96m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    print()
    print(color.GREEN + 80 * '-' + color.END)
    print(color.BOLD + "                             AUTO-MACCHANGER" + color.END)
    print(color.BOLD + color.BLUE + '                                 Blueberry' + color.END)
    print()
    print(color.RED + "This Script Depends On Macchanger Make Sure its installed before you proceed." + color.END)
    print()
    os.system("which macchanger")
    print()
    print(color.GREEN + "1.  Random Mac address" + color.END)
    print(color.GREEN + "2.  Custom Mac address " + color.END)
    print(color.GREEN + "3.  Random Mac address & Enable Monitor Mode " + color.END)
    print(color.GREEN + "4.  Custom Mac address & Enable Monitor Mode" + color.END)
    print(color.GREEN + 80 * '-' + color.END)
    print()
    choice = int(input(color.CYAN + 'Enter your choice [1-4] : ' + color.END))
    print()

    interface = input(color.RED + 'Enter Interface Name: ' + color.END)

    if choice == 1:
        os.system("sudo ifconfig {0:1} down".format(interface))
        os.system("sudo macchanger -r {0:1}".format(interface))
        os.system("sudo ifconfig {0:1} up".format(interface))

    elif choice == 2:
        coustom = input(color.RED + 'Enter Custom Mac Address: ' + color.END)
        os.system("sudo ifconfig {0:1} down".format(interface))
        os.system('sudo macchanger -m {0:1} {1:1}'.format(coustom,interface))
        os.system("sudo ifconfig {0:1} up".format(interface))

    elif choice == 3:
        os.system("sudo ifconfig {0:1} down".format(interface))
        os.system("sudo iwconfig {0:1} mode monitor".format(interface))
        os.system("sudo macchanger -r {0:1}".format(interface))
        os.system("sudo ifconfig {0:1} up".format(interface))

    elif choice == 4:
        coustom = input(color.RED + 'Enter Custom Mac Address: ' + color.END)
        os.system("sudo ifconfig {0:1} down".format(interface))
        os.system('sudo macchanger -m {0:1} {1:1}'.format(coustom,interface))
        os.system("sudo iwconfig {0:1} mode monitor".format(interface))
        os.system("sudo ifconfig {0:1} up".format(interface))

    else:
        print('Enter Option')
