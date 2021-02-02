# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:04:06 2021

@author: Demuanov
"""

import PyPDF2
import os
import tika
import re

tika.initVM()
from tika import parser

# direc = 'C:\\1\\'
# file = '2.pdf'
# path = direc + file


import pandas as pd
from tkinter import *
from tkinter import filedialog as fd

global directory1


def selectDir():
    directory1 = fd.askdirectory() + '/'
    return directory1


def startRename(directory):
    directory1 = directory.replace('/', '\\')
    files = sorted([path for path in os.listdir(directory) if os.path.isfile(directory + path)])
    i = 0

    while files:
        file = files[0]
        ext = file.split('.')[-1]
        if not os.path.isfile(f'{directory}{i}.{ext}'):
            parsed = pars(directory1 + file)
            name = f'Ведомость_{Vedomosti(file, parsed, directory1)}.{ext}'
            os.rename(directory1 + file, directory1 + name)
            del files[0]
        i += 1
    else:
        print('NO files in directory!')


def pars(path):
    # while open(path, 'rb') as f:
    path1 = path.replace('/', '\\')
    parsed = parser.from_file(path1)
    return parsed


def Vedomosti(file, parsed, directory1):
    # parsed = pars(directory1+file)
    Num_int = parsed['content'].find("№")
    fileReader = PyPDF2.PdfFileReader(directory1 + file)
    num_pages = fileReader.getNumPages()
    # print(Num_int)
    Predmet = parsed['content'].find("семестр\n") + 9
    Correct_Semestr = parsed['content'][Predmet:Predmet +30]
    print(Correct_Semestr)
    Correct_Name = parsed["content"][Num_int + 2:Num_int + 11]
    Correct_Name.replace(" ", "")
    output = f'C:\\1\\2\\Ведомость_{Correct_Name}.txt'
    with open(output, 'w') as f:
        print(parsed['content'], file=f)

    
    GroupNumber = SearchGroup(parsed)
    print(GroupNumber)
    return Correct_Name

def SearchGroup(inputPDF):
    data = inputPDF['content']
    group = re.search(r'\b\d{5}\b', data)

    if group is not None:
          return group.group()

def SearchPredmet(inputPDF):
    data = inputPDF['content']

    predmet = 'lol'

def Name(Name):
    return os.rename(path, f'{direc}Ведомость_{Name}.pdf')


root = Tk()
root.geometry('350x75')

b1 = Button(text='Выбрать папку', command=lambda: startRename(selectDir()))
b1.grid(row=0, column=1)

root.mainloop()

Name(Vedomosti(file))
print("DONE")