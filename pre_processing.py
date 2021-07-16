import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
pd.set_option('mode.chained_assignment',  None)

class data:

    def process():


        df = pd.read_csv("./dataset/범죄검거상황.csv", encoding='cp949', header=2, thousands=',')
        
        df = df[df["분류.3"] != "보험사기방지특별법"]
        del df["No"]
        del df["분류.1"]
        del df["분류.2"]
        del df["원자료.4"]
        del df["분류"]
                
        df.columns = ['통계년도', '범죄종류', '발생건수', '발생비', '검거건수', '검거율(%)', '남자', '여자', '미상']

        df["발생건수"] = df["발생건수"].astype(int)
        df["검거건수"] = df["검거건수"].astype(int)
        df["남자"] = df["남자"].astype(int)
        df["여자"] = df["여자"].astype(int)
        df["미상"] = df["미상"].astype(int)
        df["검거율(%)"] = df["검거율(%)"].round(3)
        
