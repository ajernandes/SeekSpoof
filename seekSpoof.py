import os
import tkinter as tk
from tkinter import colorchooser

version = "1.0"

# define the pre-set colors
white = '#ffffff'
green = '#00ff00'
red = '#ff0000'
blue = '#0000ff'
orange = '#ffa500'
pink = '#FA8072'
teal = '#00FFFF'
purple = '#c800c7'
yellow = '#FFFF00'

# define the patten codes
on = '07 00'
breathe = '0f 0f'
blink = '09 00'
fastslow = '01 0f'
slowfast = 'f0 01'

all = '00'
half = '03'
ten = '06'

os.system('sudo hciconfig hci0 up')
os.system('sudo hciconfig hci0 leadv 3')
os.system('sudo hciconfig hci0 noscan')

global scolor
global spattern
global sprobability
scolor = white
spattern = on
sprobability = all
hcolor = '#ffffff'


def startLight(color, pattern, probability):
    color = color.replace('#', '')
    pred = color[:2]
    pgreen = color[3:5]
    pblue = color[-2:]
    color = pgreen + ' ' + pred + ' ' + pblue
    os.system('sudo hcitool -i hci0 cmd 0x08 0x0008 1e 02 01 1a 02 0a 0c 11 07 ee 00 ' +
              color + ' ' + probability + ' ' + pattern + ' 00 00 00 00 00 00 00 00 04 09 4d 4f 42')


def killLight():
    os.system('sudo hcitool -i hci0 cmd 0x08 0x0008 1e 02 01 1a 02 0a 1f 0c 07 ee 00 00 00 00 00 00 00 07 00 00 00 00 00 00 00 04 09 4d 4f 42')


def setColor(color):
    global scolor
    bupreview = tk.Button(frameMain, text="Preview", bg=color, width=20, height=4).grid(
        row=4, column=1, sticky='N' + 'S' + 'E' + 'W')
    scolor = color


def setPattern(pattern):
    global spattern
    spattern = pattern
    print('set pattern' + pattern)


def setProbability(probability):
    global sprobability
    sprobability = probability


def colorpick():
    setColor(tk.colorchooser.askcolor()[1])

# GUI


window = tk.Tk()
window.title("Seek Spoof v" + version)
window.minsize(240, 115)
window.attributes('-fullscreen', True)

frameTitle = tk.Frame(window, height=40, bg="grey")
frameMain = tk.Frame(window, bg="white")

frameMain.columnconfigure(0, weight=1, minsize=60)
frameMain.columnconfigure(1, weight=1, minsize=60)
frameMain.columnconfigure(2, weight=1, minsize=60)
frameMain.columnconfigure(3, weight=1, minsize=60)

frameMain.rowconfigure(0, weight=1, minsize=15)
frameMain.rowconfigure(1, weight=1, minsize=15)
frameMain.rowconfigure(2, weight=1, minsize=15)
frameMain.rowconfigure(3, weight=1, minsize=15)
frameMain.rowconfigure(4, weight=1, minsize=15)

title = tk.Label(frameTitle, text="SeekSpoof", bg='grey', fg='white').pack()

# create the buttons for the color options
buwhite = tk.Button(frameMain, bg=white, width=20, height=4, command=lambda: setColor(
    white)).grid(row=0, column=0, sticky='N' + 'S' + 'E' + 'W')
bugreen = tk.Button(frameMain, bg=green, width=20, height=4, command=lambda: setColor(
    green)).grid(row=0, column=1, sticky='N' + 'S' + 'E' + 'W')
bured = tk.Button(frameMain, bg=red, width=20, height=4, command=lambda: setColor(
    red)).grid(row=1, column=0, sticky='N' + 'S' + 'E' + 'W')
bublue = tk.Button(frameMain, bg=blue, width=20, fg=white, height=4, command=lambda: setColor(
    blue)).grid(row=1, column=1, sticky='N' + 'S' + 'E' + 'W')
buorange = tk.Button(frameMain, bg=orange, width=20, height=4, command=lambda: setColor(
    orange)).grid(row=2, column=0, sticky='N' + 'S' + 'E' + 'W')
buyellow = tk.Button(frameMain, bg=yellow, width=20, height=4, command=lambda: setColor(
    yellow)).grid(row=2, column=1, sticky='N' + 'S' + 'E' + 'W')
bupink = tk.Button(frameMain, bg=pink, width=20, height=4, command=lambda: setColor(
    pink)).grid(row=3, column=0, sticky='N' + 'S' + 'E' + 'W')
bupurple = tk.Button(frameMain, bg=purple, width=20, height=4, command=lambda: setColor(
    purple)).grid(row=3, column=1, sticky='N' + 'S' + 'E' + 'W')
bupick = tk.Button(frameMain, width=20, text="Custom", height=4, command=colorpick).grid(
    row=4, column=0, sticky='N' + 'S' + 'E' + 'W')
bupreview = tk.Button(frameMain, text="Preview", width=20, height=4).grid(
    row=4, column=1, sticky='N' + 'S' + 'E' + 'W')

# create the buttons for the patten options
buon = tk.Button(frameMain, text="On", width=20, height=4, command=lambda: setPattern(
    on)).grid(row=0, column=2, sticky='N' + 'S' + 'E' + 'W')
bubreathe = tk.Button(frameMain, text="Breathe", width=20, height=4, command=lambda: setPattern(
    breathe)).grid(row=1, column=2, sticky='N' + 'S' + 'E' + 'W')
bublink = tk.Button(frameMain, text="Blink", width=20, height=4, command=lambda: setPattern(
    blink)).grid(row=2, column=2, sticky='N' + 'S' + 'E' + 'W')
bufastslow = tk.Button(frameMain, text="Fast-slow", width=20, height=4,
                       command=lambda: setPattern(on)).grid(row=3, column=2, sticky='N' + 'S' + 'E' + 'W')
buslowfast = tk.Button(frameMain, text="Slow-fast", width=20, height=4,
                       command=lambda: setPattern(on)).grid(row=4, column=2, sticky='N' + 'S' + 'E' + 'W')

# create the buttons for the other options
busettings = tk.Button(frameMain, text="Exit", width=20, height=4, command=window.destroy).grid(
    row=0, column=3, sticky='N' + 'S' + 'E' + 'W')
bustart = tk.Button(frameMain, text="Send", bg='green', width=20, height=8, command=lambda: startLight(
    scolor, spattern, sprobability)).grid(row=3, column=3, rowspan=2, sticky='N' + 'S' + 'E' + 'W')
bustop = tk.Button(frameMain, text="Stop", bg='red', width=20, height=8, command=killLight).grid(
    row=1, column=3, sticky='N' + 'S' + 'E' + 'W', rowspan=2)

frameTitle.pack(fill=tk.BOTH, side=tk.TOP, expand=False)
frameMain.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()
