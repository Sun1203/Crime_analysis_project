# Crime_analysis_project<br>

<br>

범죄("***C***"rime) 가득한 세상에서 안전한 방("***Bang***") 찾기 서비스 <br>
~~C - Bang~~

### BRANCH > [PCH](https://github.com/Sun1203/Crime_analysis_project/tree/PCH)

- 20210716 작업내용
   > 2014 ~ 2019 서울시 범죄데이터 수집 및 전처리 <br><br>
   > 서울시 자치구별 범죄발생합계 등치지역도(choropleth map) 시각화

- 20210717 작업내용
   > "피터팬의 좋은방 구하기" OpenAPI 활용 <br><br>
   > 서울시 내 부동산 매물 라이브데이터 크롤링 <br>
   > (퍼포먼스 개선 필요 / URL별로 HTML태그 인덱스 위치가 상이하여 모든 방 정보가 크롤링되지 않음) <br><br>
   > **파이프라인 구축**<br><br>
<a href='https://ifh.cc/v-6JDIUF' target='_blank'><img src='https://ifh.cc/g/6JDIUF.gif' border='0'></a>  　*pipeline.gif*<br>

- 20210718 작업내용
   > 크롤링한 방 정보별 좌표값 ES geo_point type으로 변환 후 데이터 삽입 완료<br><br>
   > 테스트 후 보안등급별로 지도에 시각화 진행

- 20210719 작업내용
   > kibana maps 활용, 보안점수별로 등급 분류 후 방 추천 및 보안 위험등급의 방 geo-point type 좌표로 지도에 맵핑<br>
   > (데이터 양이 충분하지 않아서 서울시 전체에 방 정보가 고루 맵핑되지 않음 : <br>
   > **"current_data_quantity / total_data_quantity" => 4000 / 30000)**<br><br>
   > kibana dashboard와 'map.html' 연동<br><br>
<a href='https://ifh.cc/v-wVAq9r' target='_blank'><img src='https://ifh.cc/g/wVAq9r.gif' border='0'></a>  　*map.gif*<br>

- 20210720 작업내용
   > app.py 및 map.html 구성
   > index.html merge
