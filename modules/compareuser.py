import os
import urllib.request
import json
from datetime import datetime

def compareUserntoUserm(user1,user2):
    timeNowYear = str(datetime.today().year)
    timeNowMonth = str(datetime.today().month)
    filenameUser1 = "data/commit_status/"+user1+"/"+str(timeNowYear)+"_info.json"
    filenameUser2 = "data/commit_status/"+user2+"/"+str(timeNowYear)+"_info.json"
    
    json_data=open(filenameUser1).read()
    data = json.loads(json_data) 
    User1_data = int(data[timeNowYear][timeNowMonth])
    
    json_data=open(filenameUser2).read()
    data = json.loads(json_data) 
    User2_data = int(data[timeNowYear][timeNowMonth])
    
    if User1_data > User2_data:
        print(user1+"의 데이터가 "+ str(User1_data - User2_data) + "만큼 더 많습니다.")
    elif User1_data == User2_data:
        print("요번달 커밋양이 동일합니다.")
    else:
        print(user2+"의 데이터가 "+ str(User2_data - User1_data) + "만큼 더 많습니다.")

    