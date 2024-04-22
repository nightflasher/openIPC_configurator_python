import sys, locale, platform, linecache, configparser

debug_it=0

if debug_it == 1:
    print(sys.platform)
    print(locale.getdefaultlocale())
    print(platform.system())

if  'de_DE' in locale.getdefaultlocale():
    defaultLANG = 'labels_de.lang'
else:
    defaultLANG = 'labels_en.lang'    
    
config = configparser.RawConfigParser()
config.read(defaultLANG)
print(config['basic']['language'])

fopen = defaultLANG
language = str(fopen)
print(r'Reading: '+language)

import glob
langfiles = glob.glob('*.lang')
print(langfiles)
files=0
languages=''

while files < len(langfiles):
    findlang = open(langfiles[files])
    cfglines = findlang.readlines()
    languages += cfglines[1][9:-1] + ' '
    files+=1
print('Sprachen: '+languages)

import subprocess
#subprocess.run(['scp', FILE, 'USER@SERVER:PATH'])
      
import tkinter as tk
from tkinter import *
from tkinter import ttk

top = Tk()
top.geometry('800x600+400+300')
top.title(config['basic']['windowtitle'])
top.geometry('800x600')

def ping():
    host=deviceIP.get()
    print(host)
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf8')
    if 'Request timed out.' in output or '100% packet loss' in output:
        print('NOT CONNECTED')
        pingbtn.config(style='fail.TButton')
        connect.config(state='disabled')
    else:
        print('CONNECTED')
        pingbtn.config(style='success.TButton')
        connect.config(state='active')

def sel_lang(event):
    getlanguage=GUIlanguage.get()
    selectedLANG=GUIlanguage.current()
    isLANG=langfiles[selectedLANG]
    LabelLANG.configure(text=isLANG)
    config = configparser.RawConfigParser()
    config.read(isLANG)
    connect.configure(text=config['net']['connect'])
    disconnect.configure(text=config['net']['disconnect'])
    if debug_it == 1:
        print('cfg language: '+config['basic']['language'])
        print('selected language: '+getlanguage)
        print('selected id: '+str(selectedLANG))
        print('file: '+isLANG)

    
def sel_band():
    label = LabelFREQ.cget('text')
    print(label)
    if '2.4' in label:
        LabelFREQ.configure(text=config['net']['sel5'])
        freq.configure(values=freq58list)
    if '5' in label:
        LabelFREQ.configure(text=config['net']['sel24'])
        freq.configure(values=freq24list)

def sel_freq(event):
    set_freq = freq.get()
    print(set_freq[10:-1])

style = ttk.Style()
style.theme_use('default')

style.map('fail.TButton',
          background = [('disabled', 'red'), ('!disabled', 'red')],
          foreground = [('disabled', 'black'), ('!disabled', 'grey')])

style.map('success.TButton',
          background = [('active', 'green'), ('!active', 'green')],
          foreground = [('active', 'black'), ('!active', 'grey')])

style.map('none.TButton',
          background = [('active', 'lightgrey'), ('!active', 'grey')],
          foreground = [('active', 'black'), ('!active', 'black')])

LabelLANG = ttk.Label(top, text=language)
LabelLANG.place(x=10,y=10)

GUIlanguage = ttk.Combobox(top, values=languages, state='readonly')
GUIlanguage.bind("<<ComboboxSelected>>", sel_lang)
GUIlanguage.set(config['basic']['language'])
GUIlanguage.place(x=120,y=10)

LabelDEV = ttk.Label(top, text='DEVICE')
LabelDEV.place(x=10,y=60)
devicelist = ['openIPC Camera', 'NVR Hi3536', 'radxa zero 3w']
devices = ttk.Combobox(top, values = devicelist, state='readonly')
devices.set(config['net']['hardware'])
devices.place(x=10,y=60)

LabelIP = ttk.Label(top, text='IP:')
LabelIP.place(x=198,y=60)
deviceIP = ttk.Entry(top)
deviceIP.insert(0, '192.168.0.13')
deviceIP.place(width=120,x=220,y=60)

pingbtn = ttk.Button(top, text='ping', command=ping, style='none.TButton')
pingbtn.place(width=50,x=345,y=57)

LabelPWD = ttk.Label(top, text=(config['basic']['passwd'])+':')
LabelPWD.place(x=430,y=60)
pwd = ttk.Entry(top)
pwd.insert(0, 'root pwd')
pwd.place(width=110,x=505,y=60)

connect = ttk.Button(top, text=config['net']['connect'], state='disabled')
connect.place(x=620,y=57)

disconnect = ttk.Button(top, text=config['net']['disconnect'])
disconnect.place(x=705,y=57)

freq58list = ['5180 MHz [36]'
            ,'5200 MHz [40]'
            ,'5220 MHz [44]'
            ,'5240 MHz [48]'
            ,'5260 MHz [52]'
            ,'5280 MHz [56]'
            ,'5300 MHz [60]'
            ,'5320 MHz [64]'
            ,'5500 MHz [100]'
            ,'5520 MHz [104]'
            ,'5540 MHz [108]'
            ,'5560 MHz [112]'
            ,'5580 MHz [116]'
            ,'5600 MHz [120]'
            ,'5620 MHz [124]'
            ,'5640 MHz [128]'
            ,'5660 MHz [132]'
            ,'5680 MHz [136]'
            ,'5700 MHz [140]'
            ,'5720 MHz [144]'
            ,'5745 MHz [149]'
            ,'5765 MHz [153]'
            ,'5785 MHz [157]'
            ,'5805 MHz [161]'
            ,'5825 MHz [165]'
            ,'5845 MHz [169]'
            ,'5865 MHz [173]'
            ,'5885 MHz [177]']

freq24list = ['2412 MHz [1]'
            ,'2417 MHz [2]'
            ,'2422 MHz [3]'
            ,'2427 MHz [4]'
            ,'2432 MHz [5]'
            ,'2437 MHz [6]'
            ,'2442 MHz [7]'
            ,'2447 MHz [8]'
            ,'2452 MHz [9]'
            ,'2457 MHz [10]'
            ,'2462 MHz [11]'
            ,'2467 MHz [12]'
            ,'2472 MHz [13]'
            ,'2484 MHz [14]']

FREQlist = freq58list
LabelLIST = config['net']['sel5']

LabelFREQ = ttk.Label(top, text=LabelLIST)
LabelFREQ.place(x=10,y=120)
freq = ttk.Combobox(top, values = FREQlist, state='readonly')
freq.bind("<<ComboboxSelected>>", sel_freq)
freq.set(config['net']['selfreq'])
freq.place(x=10,y=140)

freqbtn = ttk.Button(top, text='2.4/5 GHz', command=sel_band)
freqbtn.place(width=80,x=200,y=135)

top.mainloop()