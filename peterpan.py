from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import json

''' ------------------------------------------------ 01

             "피터팬의 좋은방 구하기"의 openAPI
            통해 서울시 내의 부동산 매물번호 추출

    ------------------------------------------------ '''

LAT = "37.425183~37.6312936"
LONG = "126.7665084~127.1609863"
def get_room_list(LAT, LONG):
    req_url = f"https://api.peterpanz.com/houses/markers?filter=latitude:{LAT}%7C%7Clongitude:{LONG}"
    req = requests.get(req_url)
    js = json.loads(req.text)
    room_list = [f"{i['hidx']}" for i in js]
    return room_list

seoul_room_list = get_room_list(LAT, LONG)

with open("seoul_room_list.txt", "w") as srl:
    srl.write("\n".join(seoul_room_list))


''' -------------------------------------------------------------------- 02

                    필요한 방 정보 크롤링 카테고리 : 
        [계약형태, 가격, 면적, 건물유형, 주소, 보안시설, 위도, 경도]

     URL별로 크롤링되는 방식이라 속도가 많이 느린듯, 퍼포먼스 해결 전 까지
        선책으로 크롤링된 데이터가 실시간으로 DataFrame에 반영되도록 코딩 

    -------------------------------------------------------------------- '''

with open("seoul_room_list.txt", "r") as rt:
    room_info = [i.replace("\n", "") for i in rt.readlines()]
    r_info = []    
    columns = ["매물번호", "계약형태", "가격정보", "건물유형", "면적", "행정구역", "보안시설", "위도", "경도"]
    peterpan = pd.DataFrame(columns=columns)

    for i in range(len(room_info)):
        ROOM_URL = f"https://www.peterpanz.com/house/{room_info[i]}"
        req = requests.get(ROOM_URL)
        html = req.text
        soup = BeautifulSoup(html, "html.parser")

        try:
            r_contract = soup.select("div#contract_type")[0].string                                                 # 계약형태
            r_price = soup.select("tr > td")[5].string.strip()                                                      # 가격
            r_btype = soup.select("div.column.value")[12].string.strip()                                            # 건물유형
            r_area = str(soup.select("div.column.value")[15]).split()[5].replace("m<sup>2</sup>", "")               # 면적
            r_sigudong = soup.select("div#sigudong")[0].string                                                      # 행정구역
            r_security = soup.select(".commonHouse > .row.border-top > .col-md-3.col-xs-8.column.value")\
                                    [1].string.string.strip().replace(" ", "").replace("\n", " ")                   # 보안시설
            r_lat = str(soup.select("script")[43].string).split()[77].replace("'", "").replace(";", "")             # 위도
            r_long = str(soup.select("script")[43].string).split()[81].replace("'", "").replace(";", "")            # 경도

            # info = [room_info[i], r_contract, r_price, r_btype, r_area, r_sigudong, r_security, r_lat, r_long]
            info = {"매물번호": room_info[i],
                    "계약형태": r_contract,
                    "가격정보": r_price,
                    "건물유형": r_btype,
                    "면적"    : r_area,
                    "행정구역": r_sigudong,
                    "보안시설": r_security,
                    "위도"    : r_lat,
                    "경도"    : r_long}
                    
            print(i, info)           

            peterpan = peterpan.append(info, ignore_index=True)
            peterpan.to_csv("dataset/seoul_room.csv", index=False, encoding="cp949")

        except Exception as e:
            pass

print()
print("---------------------------------------------", len(seoul_room_list), "---------------------------------------------") # property live data
print("----------------------------------------  crawling done  ----------------------------------------")
print()


''' ------------------------------------------------ 03

            크롤링한 방 정보 DataFrame으로 변환

    ------------------------------------------------ '''

print(peterpan)


# # html parsing test ▼
# with open("test.txt", "w", encoding="utf-8") as srl:
#     srl.write(soup.prettify())