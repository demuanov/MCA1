import PyPDF2
import os
import tika
import pandas as pd

from tkinter import *
from tkinter import filedialog as fd


stand = 'C:\\1\\2'
def selectDir():
    return fd.askdirectory()+'/'


def startRename(directory):

    directory1=directory.replace('/', '\\')
    files=sorted([path for path in os.listdir(directory) if os.path.isfile(directory+path)])
    i=0

    while files:
        file=files[0]
        ext=file.split('.')[-1]

        if not os.path.isfile(f'{directory}{i}.{ext}'):
            #name = f'{i}.{ext}'
            DirectoryCreate(directory1, file, ext)
            #os.rename(DirectoryCreate(directory1, file) + file , directory1+name)
            del files[0]
        i+=1

def DirectoryCreate(directory, file, ext):
    ext2=os.path.splitext(file)[0]
    Name = ext2.split('_')
    Correct_Name = Name[0] + '_' + Name[1]+'.'+ext
    path = stand + '\\' + Name[len(Name) - 1] + '\\' + Name[len(Name) - 2] + '\\' + Name[len(Name) - 4] + '\\' + Name[len(Name) - 3] + '\\'

   # // Надо разбить путь на вхождения и можно жить дальше
    try:

        if not os.path.isdir(path):
            os.makedirs(path)

        os.replace(directory+file, path+file)
        os.rename(path+file, path+Correct_Name)
    except OSError:


        print("Создать директорию %s не удалось" % path)
    else:
        print("Успешно создана директория %s" % path)




root = Tk()
root.geometry('350x75')

b1 = Button(text='Выбрать папку', command=lambda: startRename(selectDir()))
b1.grid(row=0, column=1)

root.mainloop()