from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

def book(js):

    # res = es.search(index="crime_book", body={
    #     "query": 
    #     {"match": 
    #     {
    #         "저자": js
    #     }}
    # })
    # # lee = []
    # data = res['hits']['hits']
        #     products = es.search(
        #      index       = 'dictionary',
        #      body        = {
        #          "query" : {
        #              "multi_match" : {
        #                  "query"  : search_word,
        #                  "fields" : [
        #                      "product_name",
        #                      "sub_category_name",
        #                      "creator"
        #                  ]
        #              }
        #          }
        #    }
        #  )
    res = es.search(index="crime_book", body={
        "query" : {
            "multi_match" : {
                "query": js,
                "fields" : [
                    "저자",
                    "책제목",
                    "발행처"

                    ]
            }
        }
    })
    # print(res)
    data = res['hits']['hits']
    # print(data)

    return data
# book("")