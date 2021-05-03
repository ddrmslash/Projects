# This is a Translator App using Tesseract OCR

import tkinter as tk
from tkinter.ttk import *
import sys
import os
import pyautogui
import time
import pytesseract
import subprocess
import webbrowser

root = tk.Tk()

appcanvas = tk.Canvas(root, width = 900, height = 500)
appcanvas.pack()
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry4 = tk.Entry(root)
entry5 = tk.Entry(root)
entryChnManInput = tk.Entry(root)
entryRusManInput = tk.Entry(root)
entryEngChnInput = tk.Entry(root)
entryEngRusInput = tk.Entry(root)
entryRusImgProcess = tk.Entry(root)

w = 0
h = 0
x = 0
y = 0

def paintwindow():
    subprocess.call(['C:\\Windows\\System32\\mspaint.exe'])

########################################

def screenshotCHN():
    global w
    global h
    global x
    global y
    w = entry1.get()
    h = entry2.get()
    x = entry3.get()
    y = entry4.get()

    tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    scrshCHN = pyautogui.screenshot('C:\\Users\\goro\\Desktop\\TranslatorTkinterApp\\screenshots\\Chinese.png', region=(x, y, w, h))
    text = pytesseract.image_to_string(scrshCHN, lang='chi_sim', config=tessdata_dir_config)

    ii = str(text)
    # This is for spaces when converting an image
    tt = ii.replace("\n", "")
    jj = tt.replace(" ", "")
    scshchnurl = "https://translate.google.com/?sl=zh-CN&tl=en&text=" + jj + "&op=translate"
    webbrowser.open_new_tab(scshchnurl)


def screenshotRUS():
    global w
    global h
    global x
    global y
    w = entry1.get()
    h = entry2.get()
    x = entry3.get()
    y = entry4.get()

    tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    scrshRUS = pyautogui.screenshot('C:\\Users\\goro\\Desktop\\TranslatorTkinterApp\\screenshots\\Russian.png', region=(x, y, w, h))
    text = pytesseract.image_to_string(scrshRUS, lang='rus', config=tessdata_dir_config)

    ii = str(text)
    tt = ii.replace("\n", "")
    jj = tt.replace(" ", "")
    scshrusurl = "https://translate.google.com/?sl=ru&tl=en&text=" + jj + "&op=translate" # %D0%BC%D0%B5%D1%87
    webbrowser.open_new_tab(scshrusurl)

########################################

def chnimg():
    tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    chnimgproc = entry5.get()
    chnwindowify = chnimgproc.replace('\\', "\\")
    text = pytesseract.image_to_string(chnwindowify, lang='chi_sim', config=tessdata_dir_config)

    ii = str(text)
    tt = ii.replace("\n", "")
    chnimgtxt = tt.replace(" ", "")
    chnimgurl = "https://translate.google.com/?sl=zh-CN&tl=en&text=" + chnimgtxt + "&op=translate"
    webbrowser.open_new_tab(chnimgurl)


def rusimg():
    tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    rusimgproc = entryRusImgProcess.get()
    ruswindowify = rusimgproc.replace('\\', "\\")
    text = pytesseract.image_to_string(ruswindowify, lang='rus', config=tessdata_dir_config)

    ii = str(text)
    tt = ii.replace("\n", "")
    rusimgtxt = tt.replace(" ", "")
    rusimgurl = "https://translate.google.com/?sl=ru&tl=en&text=" + rusimgtxt + "&op=translate"
    webbrowser.open_new_tab(rusimgurl)

########################################

la = tk.Label(root, text = "Size of the screenshot window:")
appcanvas.create_window(140, 50, window=la)

la2 = tk.Label(root, text = "W")
appcanvas.create_window(65, 75, window=la2)
appcanvas.create_window(100, 75, width = 50, height = 20, window=entry1)

la3 = tk.Label(root, text = "H")
appcanvas.create_window(145, 75, window=la3)
appcanvas.create_window(180, 75, width = 50, height = 20, window=entry2)

la4 = tk.Label(root, text = "X")
appcanvas.create_window(65, 105, window=la4)
appcanvas.create_window(100, 105, width = 50, height = 20, window=entry3)

la5 = tk.Label(root, text = "Y")
appcanvas.create_window(145, 105, window=la5)
appcanvas.create_window(180, 105, width = 50, height = 20, window=entry4)

la14 = tk.Label(root, text = "X,Y = Top Left of Square")
appcanvas.create_window(135, 125, window=la14)

scrshtchnbutton = tk.Button(text='Screenshot of Chinese at W,H,X,Y', command=screenshotCHN)
appcanvas.create_window(140, 160, window=scrshtchnbutton)

scrshtrusbutton = tk.Button(text='Screenshot of Russian at W,H,X,Y', command=screenshotRUS)
appcanvas.create_window(140, 195, window=scrshtrusbutton)

button1 = tk.Button(text='Bring Up Paint', command=paintwindow)
appcanvas.create_window(140, 230, window=button1)

####################################

la6 = tk.Label(root, text = "Local link to image")
appcanvas.create_window(210, 330, window=la6)
appcanvas.create_window(210, 355, width = 400, height = 20, window=entry5)

la7 = tk.Label(root, text = "C:\\Users\\NAME\\Desktop\\FOLDERNAME\\CHINESEPICTURENAME.png")
appcanvas.create_window(210, 380, window=la7)

button2 = tk.Button(text='Process Image', command=chnimg)
appcanvas.create_window(210, 415, window=button2)


la12 = tk.Label(root, text = "Local link to image")
appcanvas.create_window(670, 330, window=la12)
appcanvas.create_window(670, 355, width = 400, height = 20, window=entryRusImgProcess)

la13 = tk.Label(root, text = "C:\\Users\\NAME\\Desktop\\FOLDERNAME\\RUSSIANPICTURENAME.png")
appcanvas.create_window(670, 380, window=la13)

button2 = tk.Button(text='Process Image', command=rusimg)
appcanvas.create_window(670, 415, window=button2)

####################################

def chineseinput():
    chnmaninput = entryChnManInput.get()
    chninput = "https://translate.google.com/?sl=zh-CN&tl=en&text=" + chnmaninput + "&op=translate"
    webbrowser.open_new_tab(chninput)

# Test chinese word
# 剑

la8 = tk.Label(root, text = "Chinese to English")
appcanvas.create_window(425, 50, window=la8)

appcanvas.create_window(425, 75, width = 200, height = 20, window= entryChnManInput)

button2 = tk.Button(text='Translate to English', command=chineseinput)
appcanvas.create_window(425, 120, window=button2)


def russianinput():
    rusmaninput = entryRusManInput.get()
    rusinput = "https://translate.google.com/?sl=ru&tl=en&text=" + rusmaninput + "&op=translate"
    webbrowser.open_new_tab(rusinput)

# Cyrillic equivilent of 'Sword'
# %D0%BC%D0%B5%D1%87

la9 = tk.Label(root, text = "Russian to English")
appcanvas.create_window(425, 200, window=la9)
appcanvas.create_window(425, 225, width = 200, height = 20, window= entryRusManInput)

button2 = tk.Button(text='Translate to English', command=russianinput)
appcanvas.create_window(425, 270, window=button2)



def engchninput():
    engchnmaninput = entryEngChnInput.get()
    engchninput = "https://translate.google.com/?sl=en&tl=zh-CN&text=" + engchnmaninput + "&op=translate"
    webbrowser.open_new_tab(engchninput)

la10 = tk.Label(root, text = "English to Chinese")
appcanvas.create_window(700, 50, window=la10)
appcanvas.create_window(700, 75, width = 200, height = 20, window= entryEngChnInput)

button2 = tk.Button(text='Translate to Chinese', command=engchninput)
appcanvas.create_window(700, 120, window=button2)


def engrusinput():
    engrusmaninput = entryEngRusInput.get()
    engrusinput = "https://translate.google.com/?sl=en&tl=ru&text=" + engrusmaninput + "&op=translate"
    webbrowser.open_new_tab(engrusinput)

la11 = tk.Label(root, text = "English to Russian")
appcanvas.create_window(700, 200, window=la11)
appcanvas.create_window(700, 225, width = 200, height = 20, window= entryEngRusInput)

button2 = tk.Button(text='Translate to Russian', command=engrusinput)
appcanvas.create_window(700, 270, window=button2)

########################################

def refresh():
    os.execl(sys.executable, sys.executable, *sys.argv)

buttonREF = tk.Button(text='Refresh Window', command=refresh)
appcanvas.create_window(60, 10, window=buttonREF)


root.mainloop()