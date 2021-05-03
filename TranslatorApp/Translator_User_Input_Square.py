# This is a script that will allow you to pick the box that Tesseract OCR will interpret

# How to use:
#   After starting the script there are 3 clicks to complete the picture
#   The clicks are made in a square form:
#       Top Left
#       Top Right
#       Bottom Left

import pyautogui
import time
import pytesseract
import time
from pynput.mouse import Listener
from pynput import keyboard

# xywh
# qwer

counter = 0
q = 0
w = 0
e = 0
r = 0
hh = []
jj = []

def on_click(x, y, button, pressed):
    #listener.start()
    global q, w, e, r, counter
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        counter += 1
        if counter == 1:
            q = x
            w = y
            jj.append(y)
            #e = x - y
        if counter == 2:
            hh.append(x)
        if counter == 3:
            r = y - jj[0]
            e = hh[0] - q
            screenshotC()
            listener.stop()


def screenshotC():
    global q,w,e,r
    print(q)
    print(w)
    print(e)
    print(r)

    time.sleep(4)

    tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    scrshCHN = pyautogui.screenshot('C:\\Users\\goro\\Desktop\\TranslatorAppInterface\\screenshots\\rando.jpg', region=(q, w, e, r))
    text = pytesseract.image_to_string(scrshCHN, lang='eng', config=tessdata_dir_config)

    ii = str(text)
    # This is for spaces when converting some images
    tt = ii.replace("\n", "")
    jj = tt.replace("$", " $")
    # The Female Sign kept showing up after the fact in my tests
    bb = jj.replace("♀", "")

    print(bb)


with Listener(on_click=on_click) as listener:
    listener.join()