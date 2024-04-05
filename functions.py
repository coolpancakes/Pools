# Important functions for scripts to function. 

import os
from pathlib import Path
import time

def re_write_main():
    with open('main.py', 'w') as main:
        main.write('## Main menu for pools password manager\n\nimport login\nimport banners\nimport functions\nimport os\n\ndef main():\n    banners.banner1()\n    main_menu = input(f\'    [>] \') \n    if main_menu == \'1\':\n        login.login()\n    elif main_menu == \'2\':\n        exit()\n\n\nmain()')


def re_write_banner():
    with open('banners.py', 'w') as banner:
        banner.write('# Banners for Pools password manager.\n\nimport os\n\ndef banner1():\n    print(\'\'\'\n    coolpancakes | pools | https://github.com/coolpancakes\n    _____________ _______ ________________________________\n\n    8""""8\n    8    8 eeeee eeeee e     eeeee\n    8eeee8 8  88 8  88 8     8   "\n    88     8   8 8   8 8e    8eeee\n    88     8   8 8   8 88       88\n    88     8eee8 8eee8 88eee 8ee88\n\n        Secured with the finest encryption\n              - coolpancakes\n\n    1) Login\n    2) Exit\n\n    \'\'\')')
        re_write_main()
        os.system('del register.py')


def clear_screen():
    OS_CHECK = os.name
    if OS_CHECK == 'nt':
        os.system('cls')
    else:
        os.system('clear')






