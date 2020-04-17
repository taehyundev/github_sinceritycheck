from modules import startmain
from modules import compareuser

sw = int(input("1. 크롤링 2. 비교 : "))
if sw == 1:
    startmain.start()
else :
    ### 라이벌 이번달 Compare ###
    user1 = input("Friend1 name : ")
    user2 = input("Friend2 name : ")
    compareuser.compareUserntoUserm(user1,user2)