import PyPDF2
import os
import tika
import pandas as pd

from tkinter import *
from tkinter import filedialog as fd

def selectDir():
    return fd.askdirectory()+'/'


def startRename(directory):

    directory1=directory.replace('/', '\\')
    files=sorted([path for path in os.listdir(directory) if os.path.isfile(directory+path)])
    i=0

    while files:
        file=files[0]
        ext=file.split('.')[-1]
        ext2=os.path.splitext(file)[0]
        if not os.path.isfile(f'{directory}{i}.{ext}'):
            name = f'{i}.{ext}'
            DirectoryCreate(directory1, ext2)
            os.rename(directory1+file, directory1+name)
            del files[0]
        i+=1

def DirectoryCreate(path, file):

    Name = file.split('_')

    path= Napravlenie

    // Надо разбить путь на вхождения и можно жить дальше
    try:
        os.makedirs(path)
    except OSError:
        print("Создать директорию %s не удалось" % path)
    else:
        print("Успешно создана директория %s" % path)



root = Tk()
root.geometry('350x75')

b1 = Button(text='Выбрать папку', command=lambda: startRename(selectDir()))
b1.grid(row=0, column=1)

root.mainloop()