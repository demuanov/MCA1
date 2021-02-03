# import re module
import re
import pandas as pd
input = 'D://drop//Dropbox//20-21//Аккредитация//Scan//Новая папка//Список.xls'

x1 = pd.ExcelFile(input)
df1 = x1.parse('TDSheet')
df2 = x1.parse('Napr')


GroupNumber = 19112

for i in range(df2['Направление'].size-1):
    if GroupNumber == df2['Группа'][i]:
        Napravlenie = df2['Направление'][i]
    i += 1

print(Napravlenie)



