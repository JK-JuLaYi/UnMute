import os
import pandas as pd

data = {}
os.chdir(os.getcwd()+'\Videos')
data= (os.listdir(os.getcwd()))
writer = pd.ExcelWriter('videos_data.xlsx', engine='xlsxwriter')

for i in data:
    sheet_data=[]
    os.chdir(os.getcwd()+'\\'+i)
    files = os.listdir(os.getcwd())
    for file in files:
        file_path = os.getcwd()+'\\'+file
        file_title = file[:-4]
        sheet_data.append([file_path,file_title])
    videos = pd.DataFrame(sheet_data)
    videos.to_excel(writer, sheet_name=i , index=False, header=False)
    os.chdir('..\\')
writer.close()
