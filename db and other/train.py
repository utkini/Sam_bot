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

words = open('words.txt')
new_word = open('new_words.txt' , 'w')
w = "1"
for word in words:
    tmp = word[:len(word)-1]
    if w not in tmp:
        new_word.write(word)
        w = tmp

new_word.close()
words.close()





