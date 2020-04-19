import pandas as pd
import glob
import os
import json
import re
from modules import writecsv
from modules import writejson
from datetime import datetime

def data_integration(UserList):
    stuff_file = "data/commit_status/"
    year = str(datetime.today().year)
    report_file = "data/"+year+"_report/result.json"
    merge_info = dict()
    i =0
    for user in UserList:
        month = ["12M","11M","10M","9M","8M","7M","6M","5M","4M","3M","2M","1M"]
        fullname =stuff_file + user+"/"+year+"_info.csv"
        user_dict = dict()
        contents = str(pd.read_csv(fullname))
        for m in month:
            contents = contents.replace(m, "")
        contents = contents.replace(user, "")
        commit_num = re.findall("\d+", contents)
        print(commit_num)
        month.reverse()
        cnt =0
        for m in month:
            user_dict[m] = commit_num[cnt]
            cnt = cnt +1
        merge_info[i] = {user:user_dict}
        i = i+1
    
    print(merge_info)
    writejson.w_json(report_file, merge_info)
   