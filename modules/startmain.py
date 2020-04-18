import os
import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup
from modules import crawling
from modules import writejson
from modules import readgraph
from modules import compareuser

def start(name):
    if name == "search":
        name = input("What is your git name ?")
    url = "https://github.com/"+name
    info = crawling.commitCheck(url,timeNow)
    if not info:
        print("can't search info")
    else:
        print("<"+timeNow+"년도 "+name+"님의 깃허브 성실도"+">\n")

        ### Result comment ###
        allSum = 0
        cnt =0
        for i in range(1,len(info)+1):
            ### info[i] 번째에 커밋량이 0 일 때
            if(info[i] != 0):
                cnt = cnt + 1
                print(str(i)+ "월 contribution(s) 양 : "+str(info[i]) + " 개")
                if(i != len(info)):
                    allSum = allSum + info[i] 

        ### this Year avg commit ###
        print("깃허브 월간 평균 커밋수 : "+str(int(allSum/(cnt-1))) + "개")


        
        ### Make Textfile (JSON) ###
        data = {str(timeNow):info}
        filename = "data/commit_status/"+name+"/"
        if os.path.isdir(filename) == False:
            os.mkdir("data/commit_status/"+name+"/")
        writejson.w_json(filename+timeNow+"_info.json", data)

        ### Make Graph/ MAKE CSV ###
        #readgraph.r_graph(info,name)

month = [1,2,3,4,5,6,7,8,9,10,11,12]
timeNow = str(datetime.today().year)
