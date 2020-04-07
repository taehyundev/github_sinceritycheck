import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup
from modules import crawling
from modules import writejson
from modules import readgraph

def init():
    url = "https://github.com/"+name
    info = crawling.commitCheck(url,timeNow)

    print("<"+timeNow+"년도 깃허브 성실도"+">\n")

    ### Result comment ###
    allSum = 0
    for i in range(1,len(info)+1):
        ### info[i] 번째에 커밋량이 0 일 때
        if(info[i] != 0):
            print(str(i)+ "월 contribution(s) 양 : "+str(info[i]) + " 개")
            if(i != len(info)):
                allSum = allSum + info[i] 

    ### this Year avg commit ###
    print("깃허브 월간 평균 커밋수 : "+str(int(allSum/(len(info)-1))) + "개")

    ### Make Graph ###
    readgraph.r_graph(info)

    ### Make Textfile (JSON) ###
    data = {str(timeNow):info}
    filename = "models/commit_status/"+name+".json"
    writejson.w_json(filename, data)


month = [1,2,3,4,5,6,7,8,9,10,11,12]
timeNow = str(datetime.today().year)
name = input("What is your git name ?")
init()
