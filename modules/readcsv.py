import pandas as pd

def r_csv(path):
   df = pd.read_csv(path ,encoding='euc-kr')
   print(df)
   print(1)