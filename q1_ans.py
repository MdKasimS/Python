import zipfile as zf
import os
import pandas as pd

directory = os.getcwd()

for item in os.listdir(path='./Que1'):
    if ".zip" in item:
        with zf.ZipFile("./Que1/"+ item,"r") as zFile:
            zFile.extractall()

filesToAppend = []

for i in os.listdir():
    
    if "60d_DAM_PTPObligationBidAwards" in i:
        print(i)
        filesToAppend.append(i)
    else:
        if ".csv" in i:
            os.remove(i)
  

colData = []

for i in filesToAppend:
    df = pd.read_csv(i)
    colData.append(list(df.columns))
    print(colData[len(colData)-1])

# commonColumns = ""
# min = len(colData[0])
# for i in colData:
#     if(len(i)<min):
#         min = len(i)
#         commonColumns = i


for i in filesToAppend:
   tempDf = pd.read_csv(i)
   finalDf = pd.concat([tempDf], ignore_index=True)
              
finalDf[colData[0]] = finalDf[colData[0]].astype(str)
finalDf.to_csv("finalCSV.csv")