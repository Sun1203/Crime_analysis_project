## 01 Theme : 나쁜녀석들 <br>

**Project Goal : Crime Data Analysis**
1. ~~과거의 범죄데이터를 분석하여 2022년의 범죄발생건수 예측~~<br>
2. 서울시 내 부동산매물 데이터를 수집하고 보안점수가 높은 방 추천
3. 분석한 데이터 시각화

## 02 Team <br>

부석민 / **이재선** / 박철희

## 03 Process<br>

1. 데이터 수집 및 데이터 전처리<br>
   - _공공데이터, 피터팬의 좋은방 구하기 OpenAPI, 크롤링_<br>
   - _부동산 사이트 크롤링 후 보안시설 및 건물유형에 따라서 매물별 보안점수 부여　▼ [전체코드보기](https://github.com/Sun1203/Crime_analysis_project/blob/PCH/peterpan.py)_<br><br>
   ```
   btype = {"아파트": 3, "공동주택": 2, "단독주택": 1}
   rsecu = {"자체경비원": 7, "현관보안": 6, "CCTV": 5, "방범창": 4, "인터폰": 2, "비디오폰": 2, "카드키": 1, "-": 0}
   ```
<br>
   
2. 파이프라인 구축
   - _크롤링과 동시에 csv파일을 갱신하여 ElasticSearch로 실시간으로 데이터가 연동되도록 계획_<br>
   - _위도와 경도는 ES의 geo_point 타입으로 연동시키기 위해 dev tools에서 파이프라인 구축 전 미리 geo_point 타입으로 맵핑_
   
<br><p align="center"><a href='https://ifh.cc/v-6JDIUF' target='_blank'><img src='https://ifh.cc/g/6JDIUF.gif' border='0'></a><a href="https://ibb.co/VgvwKc1"><img src="https://i.ibb.co/m9HNxVj/image.png" alt="image" border="0" height="300px" width="600px"></a><br><p><br>

3. 시각화
   - _geo_point 타입으로 맵핑된 데이터를 통해 kibana maps에 시각화_<br>
   
   
- 20210719 작업내용
   > kibana maps 활용, 보안점수별로 등급 분류 후 방 추천 및 보안 위험등급의 방 geo-point type 좌표로 지도에 맵핑<br>
   > (데이터 양이 충분하지 않아서 서울시 전체에 방 정보가 고루 맵핑되지 않음 : <br>
   > **"current_data_quantity / total_data_quantity" => 4000 / 30000)**<br><br>
   > kibana dashboard와 'map.html' 연동<br><br>
<a href='https://ifh.cc/v-wVAq9r' target='_blank'><img src='https://ifh.cc/g/wVAq9r.gif' border='0'></a>  　*map.gif*<br>

- 20210720 작업내용
   > app.py 및 map.html 구성<br><br>
   > index.html merge
