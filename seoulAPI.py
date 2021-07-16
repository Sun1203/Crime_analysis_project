import requests
import pandas as pd
from requests.api import request

MY_KEY = "6f62554f5a636a6638365056535078"
url = f"http://openapi.seoul.go.kr:8088/{MY_KEY}/json/SdeTlSccoSigW/1/25"

def latlng(url, coordinate):
    try:
        all_data = requests.get(url).json()
        lat_lng = all_data[coordinate]["row"]

    except:
        print("API usning failed")

    return lat_lng

data = latlng(url, "SdeTlSccoSigW")
columns = ["SIG_CD", "SIG_KOR_NM", "LAT", "LNG"]
lat_lng_data = pd.DataFrame(data, columns=columns)
lat_lng_data.columns = ["시군구코드", "시군구명",  "위도", "경도"]

lat_lng_data.to_csv("seoul_coordinate.csv", index=False)