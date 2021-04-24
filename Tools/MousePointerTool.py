
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

import time

mouse = MouseController()

time.sleep(3)

while True:
    print('mouse.position = {0}'.format(mouse.position))
    #print('mouse.release(Button.left)')
    #print('mouse.press(Button.left)')
    #print('time.sleep(.05)')
    #print("")
    #print('mouse.position = {0}'.format(mouse.position))
    time.sleep(1)

