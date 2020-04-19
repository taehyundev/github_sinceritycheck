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
    no_M =0
    no_N =0
    for user in UserList:
        month = ["12M","11M","10M","9M","8M","7M","6M","5M","4M","3M","2M","1M"]
        fullname =stuff_file + user+"/"+year+"_info.csv"
        user_dict = dict()
        contents = str(pd.read_csv(fullname))
        
        ### 내용 정리 - 월표시 없애기
        for m in month:
            contents = contents.replace(m, "")
        
        ### 정수만 추출
        commit_num = re.findall("\d+", contents)
        
        ### 그리디 형태로 월표시 제거를 했으므로 reverse하기
        month.reverse()

        ### 데이터 담기
        for m in month:
            user_dict[m] = commit_num[no_N]
            no_N = no_N +1
        merge_info[i] = {user:user_dict}
        no_M = no_M+1
    
    print(merge_info)
    ### make json 
    writejson.w_json(report_file, merge_info)
   