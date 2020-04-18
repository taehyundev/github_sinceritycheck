import os
import urllib.request
import json
from datetime import datetime
from modules import startmain
def compareUserntoUserm(user1,user2):
    timeNowYear = str(datetime.today().year)
    timeNowMonth = str(datetime.today().month)
    filenameUser1 = "data/commit_status/"+user1+"/"+str(timeNowYear)+"_info.json"
    filenameUser2 = "data/commit_status/"+user2+"/"+str(timeNowYear)+"_info.json"
    
    if os.path.isdir("data/commit_status/"+user1+"/") == True and os.path.isdir("data/commit_status/"+user1+"/") == True:
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

    else:
        print("사용자에 대한 정보가 크롤링되어있지 않습니다.")
        print("크롤링할 User를 선택해주세요.")
        print("1."+user1+" 2."+user2+" 3.All select: " )
        sw = int(input())
        if sw ==   1:
            startmain.start(user1)
        elif sw == 2:
            startmain.start(user2)
        else:
            startmain.start(user1)
            startmain.start(user2)
        compareUserntoUserm(user1,user2)
        