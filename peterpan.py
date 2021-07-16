from selenium import webdriver
from bs4 import BeautifulSoup
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
    room_list = [f"{i['hidx']}" for i in js ]
    return room_list

seoul_room_list = get_room_list(LAT, LONG)

with open("seoul_room_list.txt", "w") as srl:
    srl.write("\n".join(seoul_room_list))


''' ------------------------------------------------ 02

               필요한 방 정보 크롤링 카테고리 : 
[계약형태, 가격, 면적, 건물유형, 주소, 보안시설, 위도, 경도]

    ------------------------------------------------ '''

# with open("seoul_room_list.txt", "r") as srl:

ROOM_URL = "https://www.peterpanz.com/house/11744125"
req = requests.get(ROOM_URL)
html = req.text
soup = BeautifulSoup(html, "html.parser")
# print(len(seoul_room_list))

contract = soup.select("div#contract_type")[0].string
price = soup.select("tr > td")[5].string.strip()
sigudong = soup.select("div#sigudong")[0].string
print(price)




# html parsing test ▼
# with open("test.txt", "w", encoding="utf-8") as srl:
#     srl.write(soup.prettify())


        
        
        

