from pymongo import MongoClient
import pymongo

import re

def word_search(mess):
    with MongoClient('localhost',27017) as client:
        db = client.db_orf
        coll = db.orf_coll
        reg = '^' + mess
        lose_word = ''
        mens = coll.find({"word": {"$regex": reg}})
        for men in mens:
            word = men['word']
            if (len(word)-len(mess)) % 2 == 0:
                return word
            else:
                lose_word = word
        return lose_word

# wrd = input('Введи слово \n')
# print(word_search(wrd))
