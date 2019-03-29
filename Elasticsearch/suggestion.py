# PUT fiverr
# {
#   "mappings": {
#     "medicine": {
#       "properties": {
#         "brand": {
#           "type": "completion"
#         }
#       }
#     }
#   }
# }


# POST fiverr/medicine
# {
#   "brand": {
#     "input": ["Crocin"]
#   }
# }

from elasticsearch import Elasticsearch
import sys

ES_HOST = {"host": "localhost", "port": 9200}
es = Elasticsearch(hosts=[ES_HOST])

medicine = sys.argv[1]

body = {
  "suggest": {
    "movie-suggest": {
      "prefix": medicine,
      "completion": {
        "field": "brand",
        "fuzzy": {
          "fuzziness": 1
        }
      }
    }
  }
}

res = es.search(index="fiverr", doc_type="medicine", body=body)
try:
  print(res["suggest"]["movie-suggest"][0]["options"][0]["text"])
except Exception as ex:
  print("Result not found!")




