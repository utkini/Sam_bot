from pymongo import MongoClient
import pymongo

import re

# ДЛЯ ОТСЕИВАНИЯ НЕНУЖНЫХ СЛОВ В ФАЙЛЕ ДЛЯ ИГРЫ "БАЛДА"
# ==========================
# words = open('orf_2.txt')
# new_word = open('new_words.txt' , 'w')
# w = "1"
# for word in words:
#     tmp = word[:len(word)-1]
#     if w not in tmp:
#         new_word.write(word)
#         w = tmp
#
# new_word.close()
# words.close()


d = {'d': True,
     'b': True,
     'v': False}
di = (map(lambda x: False, list(d.values())))
print(di)




