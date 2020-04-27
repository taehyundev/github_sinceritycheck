from modules import startmain
from datetime import datetime
def allCrawlingName(UserList):
    print(1)
    timeNow = str(datetime.today().year)
    for i in range(0,len(UserList)):
        url = "https://github.com/"+UserList[i]
        startmain.start(UserList[i])

    print("총 "+ str(len(UserList)) +"개의 정보를 크롤링하였습니다.")
    print("Sucess")