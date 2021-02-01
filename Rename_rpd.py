import os

from tkinter import *
from tkinter import filedialog as fd


def selectDir():
    return fd.askdirectory() + '/'


def startRename(directory):
    directory1 = directory.replace('/', '\\')
    files = sorted([path for path in os.listdir(directory) if os.path.isfile(directory + path)])

    for file in files:
        os.rename(directory1 + file, directory1 + "01.03.01_РПД_" + file)


root = Tk()
root.geometry('350x75')

b1 = Button(text='Выбрать папку', command=lambda: startRename(selectDir()))
b1.grid(row=0, column=1)

root.mainloop()
