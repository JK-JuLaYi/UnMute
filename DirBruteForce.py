import os
import pandas as pd
from openpyxl import Workbook


folders = os.walk('F:\\AI\\UnMute\\Dataset\\Videos')
number_folders = len(next(folders)[1])

writer = pd.ExcelWriter('F:\\AI\\UnMute\\Dataset\\Docs\\FilePaths.xlsx',engine='openpyxl')

for i in range(number_folders):
    sub_dir = next(folders)
    dir,files = sub_dir[0],sub_dir[2]
    file_path = []
    for file in files:
        file_path.append(dir+'\\'+file)
    
    df = pd.DataFrame(file_path)
    
    
    
    dir_name = dir.split('\\')[-1]

    df.to_excel(writer,sheet_name= dir_name,index = False,header = None)
writer.close()
