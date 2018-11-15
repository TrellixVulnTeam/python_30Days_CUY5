import json
from collections import namedtuple
y= '[ {"key": "database_administration","doc_count": 2}, {"key": "networks","doc_count": 2} ]'
x = json.loads(y, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
z={}
z[0] = { x[0].key : x[0].doc_count } 
for i in range(0,len(x),1):
    z[i] = { x[i].key : x[i].doc_count } 

class ABC:
    key=x[0].key,
    doc=x[0].doc_count

y= [{"key": "database_administration","doc_count": 2}, {"key": "networks","doc_count": 2}]
x = {}
for i in range(len(y)):
    key = y[i]["key"]
    val = y[i]["doc_count"]
    x[key] = val

