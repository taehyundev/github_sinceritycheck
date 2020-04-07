from matplotlib import pyplot as plt
import pandas as pd
from modules import writecsv
from modules import readcsv

def r_graph(info,name):
    month = list()
    value = list()
    month= list()
    csvinfo = list()

    for i in range(12):
        month.append(str(i+1) + "M")
    for i in range(1, len(info)+1):    
       if info[i] != 0:
           value.append(info[i])
    print(value)
    for i in range(len(info), 12):
        value.append(0)
    
    for i in range(12):
       csvinfo.append([month[i], value[i]])
    print(csvinfo)

    ### csv 파일 생성 시각화 자료
    filename = "data/commit_status/"+name+".csv"
    writecsv.w_csv(filename, csvinfo)
    
    ### Read CSV ### 
    readcsv.r_csv("data/commit_status/"+name+".csv")
    
    ### Read graph ###
    plt.bar(month, value, label="Set 1", color= 'b')
    plt.legend()
    plt.title(name + " Chart")
    plt.show()

