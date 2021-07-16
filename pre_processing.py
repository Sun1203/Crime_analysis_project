import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
pd.set_option('mode.chained_assignment',  None)

class data:

    def process():

        # 범죄 발생과 범죄 검거 상황 정제

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

        # 범죄 검거까지 기간 데이터 정제

        df1 = pd.read_csv("./dataset/범죄검거기간.csv", encoding='cp949', header=2, thousands=',')

        df1 = df1[df1["분류.1"] != "강간·강제추행"]

        del df1["분류"]
        del df1["원자료.10"]
        del df1["원자료"]
        del df1["No"]

        df1.columns = ['통계년도', '범죄종류', '1일이내', '2일이내', '3일이내', '10일이내', '1개월이내', '3개월이내', '6개월이내', '1년이내', '1년초과']

        df1["1일이내"] = df1["1일이내"].astype(int)
        df1["2일이내"] = df1["2일이내"].astype(int)
        df1["3일이내"] = df1["3일이내"].astype(int)
        df1["10일이내"] = df1["10일이내"].astype(int)
        df1["1개월이내"] = df1["1개월이내"].astype(int)
        df1["3개월이내"] = df1["3개월이내"].astype(int)
        df1["6개월이내"] = df1["6개월이내"].astype(int)
        df1["1년이내"] = df1["1년이내"].astype(int)
        df1["1년초과"] = df1["1년초과"].astype(int)