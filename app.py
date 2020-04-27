from modules import startmain
from modules import compareuser
from modules import allcrawling
from modules import getuserlist
from modules import dataintegration
import os

while True:
    sw = int(input("0. 전체 크롤링\n1. 크롤링 \n2. 비교 \n3. 크롤링 유저 리스트\n4. 이번년도 데이터 합치기 \n>>> "))
    if sw ==0:
        UserList =getuserlist.get_userList()
        print(UserList)
        allcrawling.allCrawlingName(UserList)
    elif sw == 1:
        startmain.start("search")
    elif sw ==2 :
        ### 라이벌 이번달 Compare ###
        user1 = input("Friend1 name : ")
        user2 = input("Friend2 name : ")
        compareuser.compareUserntoUserm(user1,user2)
    elif sw ==3:
        UserList =getuserlist.get_userList()
        print("user list : "+str(UserList))
    elif sw ==4:
        UserList =getuserlist.get_userList()
        dataintegration.data_integration(UserList)
    else :
        continue

