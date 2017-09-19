from pymongo import MongoClient

"""
Этот класс предназначен для записи всех слов всех пользователей в БД (многопоточность)
"""


class UserWord():
    def __init__(self):
        with MongoClient('localhost', 27017) as client:
            db = client.db_userwords
            self.coll = db.coll_users

    def create_new_user(self, username, user_id):
        d = {'username': username,
             'user_id': user_id,
             'session': ""}
        self.coll.insert(d)

    def update_word(self, username ,user_id, word):
        self.coll.update({'username': username,
                          'user_id': user_id},
                         {'$set': {'session': word}})

    def get_word(self, username, user_id):
        sample = self.coll.find_one({'username': username,
                                     'user_id': user_id})
        word = sample['session']
        return word


