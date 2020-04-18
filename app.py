from modules import startmain
from modules import compareuser
import os

while True:
    sw = int(input("1. 크롤링 \n2. 비교 \n3. 크롤링 유저 리스트\n >>> "))
    if sw == 1:
        startmain.start("search")
    elif sw ==2 :
        ### 라이벌 이번달 Compare ###
        user1 = input("Friend1 name : ")
        user2 = input("Friend2 name : ")
        compareuser.compareUserntoUserm(user1,user2)
    elif sw ==3:
        files = os.listdir("data/commit_status/")
        UserList = list()
        for User in files:
            UserList.append(User)
        print("user list : "+str(UserList))
