import os
def get_userList():
    UserList = list()
    files = os.listdir("data/commit_status/")
    for User in files:
        UserList.append(User)
    return UserList