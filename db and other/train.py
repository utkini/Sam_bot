from pymongo import MongoClient
import pymongo

import re

# wrd = input('Введи слово \n')
# print(word_search(wrd))

# def sepr(mess):
#     mess = mess.lower()
#     for c in mess:
#         if ord(c)<1040 or ord(c)>1103:
#             return 'Вы ввели что-то не то'
#     return  'Все хорошо'
#
# mess = input()
# print(sepr(mess))

with open('words.txt') as words, open('new_words.txt' , 'w') as new_word:
    for i,w in enumerate(words):
        word_one = w.rstrip('\n')



