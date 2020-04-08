import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup

def commitCheck(url, timeNow):
    info = dict()
    month = [1,2,3,4,5,6,7,8,9,10,11,12]
    response = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(response, 'html.parser')

    ### class가 day인 부분 찾기 ###
    title =soup.find_all(class_='day')
    
    ### 원하는 정보 추출 ###
    for i in title:
        # 커밋 올린 년,월,일 나타내기
        commitYear = i["data-date"][0]+i["data-date"][1]+i["data-date"][2]+i["data-date"][3]
        commitMonth = int(i["data-date"][5] + i["data-date"][6])
        commitDay = int(i["data-date"][8] + i["data-date"][9])
        if commitYear == timeNow:
            if(commitDay == 1):
                info[commitMonth] =0
            info[commitMonth]  =  info[commitMonth] +int (i["data-count"])
    
    return info
