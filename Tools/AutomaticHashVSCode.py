from pynput.keyboard import Key, Controller as KeyboardController
import time

keys = KeyboardController()

tt = int(input())
time.sleep(5)
for x in range (1,tt+1):
    keys.press(Key.shift)
    keys.press('3')
    keys.release('3')
    keys.release(Key.shift)
    keys.press(Key.left)
    keys.press(Key.down)
    time.sleep(.01)
