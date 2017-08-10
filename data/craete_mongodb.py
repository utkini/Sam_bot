import pymongo
from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client.db_orf
coll = db.orf_coll

# Ввод нужных значений в нашу базу данных
coll.remove(None)
with open('words.txt') as f:
    id = 0
    for l in f:
        line = l.rstrip('\n')
        d = { 'id' :str(id), 'word' : line}
        coll.insert(d)
        id += 1
i = 0
for men in coll.find():
    i += 1
    print(men)
    if i > 40:
        break
