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
   - _크롤링과 csv파일 갱신을 동시에 진행하여 ElasticSearch로 실시간으로 데이터가 삽입되도록 계획_<br>
   - _위도와 경도는 ES의 geo_point 타입으로 사용하기 위해 파이프라인 구축 전 미리 dev tools에서 geo_point 타입으로 맵핑_
   
<p align="center"><a href='https://ifh.cc/v-6JDIUF' target='_blank'><img src='https://ifh.cc/g/6JDIUF.gif' border='0'></a><a href="https://ibb.co/VgvwKc1"><img src="https://i.ibb.co/m9HNxVj/image.png" alt="image" border="0" height="300px" width="600px"></a><br><p><br>

3. 시각화
   - _geo_point 타입으로 맵핑된 데이터를 통해 kibana maps에 시각화_<br>
   - _부여한 보안점수별로 구간(등급)을 나눠 사용자가 필터링할 수 있도록 계획_<br>
   - _매물별 URL을 하이퍼링크타입으로 변환하여 맵핑된 지도와 부동산매물사이트 연계_
<p align="center"><a href='https://ifh.cc/v-wVAq9r' target='_blank'><img src='https://ifh.cc/g/wVAq9r.gif' border='0' height="400px" width="600px"></a></p>
   

4. Flask
   - _시각화된 결과물을 kibana dashboard로 정리 후 html 코드로 변환하여 웹페이지로 제작_<br>
