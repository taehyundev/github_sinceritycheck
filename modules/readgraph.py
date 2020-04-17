import os
from matplotlib import pyplot as plt
from datetime import datetime
import pandas as pd
from modules import writecsv
from modules import readcsv

def r_graph(info,name):
    month = list()
    value = list()
    month= list()
    csvinfo = list()
    timeNow = str(datetime.today().year)

    for i in range(12):
        month.append(str(i+1) + "M")
    for i in range(1, len(info)+1):    
        if info[i] != None:
           value.append(info[i])
    print(value)
    for i in range(len(info), 12):
        value.append(0)
    
    for i in range(12):
       csvinfo.append([month[i], value[i]])
    print(csvinfo)

    ### csv 파일 생성 시각화 자료
    filename = "data/commit_status/"+name+"/"
    
    if os.path.isdir(filename) == False:
        os.mkdir("data/commit_status/"+name+"/")
    writecsv.w_csv(filename+timeNow+"_info.csv", csvinfo)
    print("성공")
    
    ### Read CSV ### 
    readcsv.r_csv(filename+timeNow+"_info.csv")
    
    ### Read graph ###
    plt.bar(month, value, label="Set 1", color= 'b')
    plt.legend()
    plt.title(name + " Chart")
    plt.show()

