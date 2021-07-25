## 01 Theme : 나쁜녀석들 <br>

**Project Goal : Crime Data Analysis**
1. ~~과거의 범죄데이터를 분석하여 2022년의 범죄발생건수 예측~~<br>
2. 서울시 내 부동산매물 데이터를 수집하고 보안점수가 높은 방 추천
4. 범죄자와 피해자의 데이터를 정제 분석후 시각화
5. 범죄에 관련된 책에 대한 정보를 검색후 정보 전달
6. 회원가입 기능 구현(flask & Oracle DB)
7. 로그인 기능 구현(jwt & flask & Oracle DB)
8. ~~글쓰기 기능~~



## 02 Team <br>

**부석민 / 이재선 / 박철희**

## 03 Process<br>

1. 데이터 수집 및 데이터 전처리<br>
   - _공공데이터, 피터팬의 좋은방 구하기 OpenAPI, 크롤링_<br>
   - _부동산 사이트 크롤링 후 보안시설 및 건물유형에 따라서 매물별 보안점수 부여　▼ [전체코드보기](https://github.com/Sun1203/Crime_analysis_project/blob/PCH/peterpan.py)_<br>
   - _공공데이터 [CCJS](https://www.crimestats.or.kr/portal/stat/easyStatPage.do) 사이트에서 데이터 수집_<br><br>
  ```
   btype = {"아파트": 3, "공동주택": 2, "단독주택": 1}
   rsecu = {"자체경비원": 7, "현관보안": 6, "CCTV": 5, "방범창": 4, "인터폰": 2, "비디오폰": 2, "카드키": 1, "-": 0}
   ```
   
<br>
   
2. 파이프라인 구축
   - _크롤링과 csv파일 갱신을 동시에 진행하여 ElasticSearch로 실시간으로 데이터가 삽입되도록 계획_<br>
   - _위도와 경도를 ES의 geo_point 타입으로 사용하기 위해 파이프라인 구축 전 dev tools에서 location 필드를 geo_point 타입으로 맵핑_
   
<p align="center"><a href='https://ifh.cc/v-6JDIUF' target='_blank'><img src='https://ifh.cc/g/6JDIUF.gif' border='0'></a><br><br>
   <a href="https://ibb.co/VgvwKc1"><img src="https://i.ibb.co/m9HNxVj/image.png" alt="image" border="0" height="300px" width="600px"></a><br><p><br>

3. 시각화
   - _geo_point 타입으로 맵핑된 데이터를 통해 kibana maps에 시각화_<br>
   - _부여한 보안점수별로 구간(등급)을 나눠 사용자가 필터링할 수 있도록 계획_<br>
   - _매물별 URL을 하이퍼링크타입으로 변환하여 맵핑된 지도와 부동산매물사이트 연계_<br>
   - _범죄 발생건수, 검거율, 검거기간 등 연관있는 데이터들로 kibana 시각화후 대시보드에 합침_<br>
<p align="center"><a href='https://ifh.cc/v-wVAq9r' target='_blank'><img src='https://ifh.cc/g/wVAq9r.gif' border='0' width="800px"></a></p><br>
   

4. Flask
   - _시각화된 결과물을 kibana dashboard로 정리 후 html 코드로 변환하여 웹페이지로 제작_<br>
   - _회원가입 기능, 로그인기능(jwt) 구현_
   - _토크나이저는 한글 형태소분석기인 노리(nori) 형태소 분석기를 이용했고, 자동완성 구현을 위해 edge_ngram filter를 이용하였다_<br><br>
   ```
        const $app = document.getElementById('App')

     data.forEach(element => {
         data = element['_source']

         Object.keys(data).forEach(key => {

             const $testDOM = document.createElement('div')

             $testDOM.innerHTML = key + ' : ' + data[key]

             $app.appendChild($testDOM)
         })
     })
     ```

<br>

5. 파일별 기능 개요
   - _pre-preocess.py : CCJS 데이터 전처리 및 데이터프레임 생성_ 
   - _Elk_python.py   : ElasticSearch와 python을 연결하고 쿼리 작성_ 
   - _peterpan.py     : 피터팬의 좋은방 구하기 크롤러_ 
   - _dto.py          : 각 컬럼항목 저장 및 컬럼을 하나의 클래스에 매칭_
   - _Db_dao.py       : dto.py에 정보 저장_.
   
