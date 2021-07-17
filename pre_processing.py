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


        # 범죄자의 금전소비 용도 데이터 정제

        df2 = pd.read_csv("./dataset/금전소비용도.csv", encoding='cp949', header=2, thousands=',')

        df2 = df2[df2["분류"] != "계"]

        del df2["No"]
        del df2["분류"]
        del df2["원자료"]
        del df2["분류.1"]

        df2.columns = ["통계년도", "범죄종류", "유흥", "오락", "생활비", "도박", "학비", "증여", "소지중", "기타", "미상"]


        # 범죄자 범행시 정신 상태 정제

        df3 = pd.read_csv("./dataset/범죄자범행시정신상태.csv", encoding='cp949', header=2, thousands=',')

        del df3["No"]
        del df3["분류"]
        del df3["분류.1"]
        del df3["계"]
        del df3["남자(계)"]
        del df3["여자(계)"]
        del df3["정상(남)"]
        del df3["정상(여)"]
        del df3["정신이상(소계)"]
        del df3["정신이상(남)"]
        del df3["정신이상(여)"]
        del df3["정신박약(소계)"]
        del df3["정신박약(남)"]
        del df3["정신박약(여)"]
        del df3["기타정신장애(소계)"]
        del df3["기타정신장애(남)"]
        del df3["기타정신장애(여)"]
        del df3["주취(남)"]
        del df3["주취(여)"]
        del df3["월경시이상"]

        df3 = df3[df3["자료시점"] != "자료시점"]
        df3.columns = ['발생년도', '범죄종류', '정상', '정신장애', '주취', '미상']

        df3["정상"] = df3["정상"].apply(lambda x: x.replace(',', ''))
        df3["정신장애"] = df3["정신장애"].apply(lambda x: x.replace(',', ''))
        df3["주취"] = df3["주취"].apply(lambda x: x.replace(',', ''))
        df3["미상"] = df3["미상"].apply(lambda x: x.replace(',', ''))

        df3["정상"] = df3["정상"].astype(int)
        df3["정신장애"] = df3["정신장애"].astype(int)
        df3["주취"] = df3["주취"].astype(int)
        df3["미상"] = df3["미상"].astype(int)


        # 범죄자 성별 데이터 정제

        df4 = pd.read_csv("./dataset/범죄자성.csv", encoding='cp949', header=2, thousands=',')

        del df4["No"]
        del df4["분류"]
        del df4["분류.1"]
        del df4["원자료"]
        del df4["원자료.4"]

        df4.columns = ['발생년도', '범죄종류', '남자', '여자', '미상']
        

        