# Import pandas
import pandas as pd
import os
import shutil


# Assign spreadsheet filename to `file`
file = 'C://Users//Demuanov//Desktop//123.xlsx'


# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
list_name = '02.04.01  '
directory = 'C://2020/'
path_finish = f'C://2020//{list_name}'
if not os.path.exists(path_finish): os.makedirs(path_finish)
df1 = xl.parse(list_name)

#print(df1)
#print(df1['ФИО'][0])
names_from_excell = df1['ФИО'].tolist()
files = sorted([path for path in os.listdir(directory) if os.path.isfile(directory+path)])



i=0
files1 = []
for i in files:
        #files_in_folder = files[i]
        ext = i.split('-')
        files1.append(ext[0])

print(files1[0])

for x in names_from_excell:
     for y in files1:
         if y == x:
             number = files1.index(y)
             path_start = f'C://2020//{files[number]}'
             shutil.copy(path_start, path_finish)
             files1[number] = 'NaN'
f = open( f'{list_name}.txt', 'w' )
for item in files1:
    f.write("%s\n" % item)





print('Hell!')


#os.makedirs()