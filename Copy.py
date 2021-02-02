from __future__ import print_function
import os
import re
import pandas as pd

#input = 'C:\\1\\2\\Ведомость_000051626.txt'

input = 'D://drop//Dropbox//20-21//Аккредитация//Scan//Новая папка//Список.xls'

x1 = pd.ExcelFile(input)

print(x1.sheet_names)

df1 = x1.parse('TDSheet')
df1_Vedomosti =  df1['Номер']

print(df1)
print(df1_Vedomosti[0])

with open(input) as o:
    data = o.readlines()

for i in data:
    result = re.search(Substring, i)
    if result is not None:
           print(result.group())

