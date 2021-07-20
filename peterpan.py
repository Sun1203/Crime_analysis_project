from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import json


''' -------------------------------------------------------------------- 01

                      "피터팬의 좋은방 구하기"의 openAPI
                     통해 서울시 내의 부동산 매물번호 추출

    -------------------------------------------------------------------- '''

# LAT = "37.425183~37.6312936"
# LONG = "126.7665084~127.1609863"
# def get_room_list(LAT, LONG):
#     req_url = f"https://api.peterpanz.com/houses/markers?filter=latitude:{LAT}%7C%7Clongitude:{LONG}"
#     req = requests.get(req_url)
#     js = json.loads(req.text)
#     room_list = [f"{i['hidx']}" for i in js]

#     return room_list

# seoul_room_list = get_room_list(LAT, LONG)

# with open("seoul_room_list.txt", "w") as srl:
#     srl.write("\n".join(seoul_room_list))


''' -------------------------------------------------------------------- 02

                      필요한 방 정보 크롤링 카테고리 : 
        [계약형태, 가격, 면적, 건물유형, 보안시설, 위도, 경도]

  URL별로 원하는 정보의 HTML tag 위치가 조금씩 상이함... try, except로 처리

   URL별로 크롤링되는 방식이라 속도가 많이 느린듯... 퍼포먼스 해결 전 까지
     차선책으로 크롤링된 데이터가 실시간으로 DataFrame에 반영되도록 코딩 

    -------------------------------------------------------------------- '''


with open("seoul_room_list.txt", "r") as rt:
    room_info = [i.replace("\n", "") for i in rt.readlines()]
    columns = ["매물번호", "계약형태", "가격정보", "건물유형", "면적", "보안시설", "보안점수", "시구동", "위도", "경도", "링크"]
    peterpan = pd.DataFrame(columns=columns)
    loop_range = int(len(room_info))

    for i in range(11862, 12862):
        ROOM_URL = f"https://www.peterpanz.com/house/{room_info[i]}"
        req = requests.get(ROOM_URL)
        html = req.text
        soup = BeautifulSoup(html, "html.parser")

        # html parsing test ▼
        # with open("test.txt", "w", encoding="utf-8") as srl:
        #     srl.write(soup.prettify())

        try:
            r_contract = soup.select("div#contract_type")[0].string                                                                 # 계약형태
            r_price = soup.select("tr > td")[5].string.strip()                                                                      # 가격
            r_btype = soup.select("div.column.value")[12].string.strip()                                                            # 건물유형
            r_area = float(str(soup.select("div.column.value")[15]).split()[5].replace("m<sup>2</sup>", ""))                        # 면적
            r_security = soup.select(".commonHouse > .row.border-top > .col-md-3.col-xs-8.column.value")\
                                     [1].string.string.strip().replace(" ", "").replace("\n", " ").replace(",", " ").split()        # 보안시설
            r_sigudong = soup.select("div#sigudong")[0].string                                                                      # 시구동
            r_lat = float(str(soup.select("script")[44].string).split()[77].replace("'", "").replace(";", ""))                      # 위도
            r_long = float(str(soup.select("script")[44].string).split()[81].replace("'", "").replace(";", ""))                     # 경도

            btype = {"아파트": 3, "공동주택": 2, "단독주택": 1}
            rsecu = {"자체경비원": 7, "현관보안": 6, "CCTV": 5, "방범창": 4, "인터폰": 2, "비디오폰": 2, "카드키": 1, "-": 0}
            r_score = 0                                                                                                             # 보안점수

            for j in btype:
                if r_btype == j:
                    r_score = btype[j]    
            
            for j in r_security:
                r_score += rsecu[j]

            r_security = " / ".join(r_security)

            info = {"매물번호" : room_info[i],
                    "계약형태" : r_contract,
                    "가격정보" : r_price,
                    "건물유형" : r_btype,
                    "면적"     : r_area,
                    "보안시설" : r_security,
                    "보안점수" : r_score,
                    "시구동"   : r_sigudong,
                    "위도"     : r_lat,
                    "경도"     : r_long,
                    "링크"     : ROOM_URL}

            print(f"[{loop_range}/{i}] : {room_info[i]}", info)           
            # print(f"[{loop_range}/{i}] Crawling in progress")           

            peterpan = peterpan.append(info, ignore_index=True)                                                                    # 파이프라인 구축
            peterpan.to_csv("dataset/seoul_room.csv", index=False, encoding="utf-8", header=False)                                 # header 없이 csv에 저장 => logstash & beats를 통해 ES에 데이터 실시간 insert

        except:
            print(f"[{loop_range}/{i}] : {room_info[i]}", "crawling failed")
            # print(f"[{loop_range}/{i}] Crawling in progress")

print()
print("----------------------------------------  crawling done  ----------------------------------------")
print()