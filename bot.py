import telebot
from telebot import types
import requests
import config
import data
import search_word

token = config.token
bot = telebot.TeleBot(token)

def lower(text):
    return text.lower()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome = data.welcome(message)
    bot.reply_to(message,welcome)

@bot.message_handler(commands=['help'])
def helper(message):
    helpr = data.helper(message)
    bot.send_message(message.chat.id, helpr)

@bot.message_handler(regexp='Какое слово')
def answer(message):
    bot.send_message(message.chat.id,balda.get_word())

balda = search_word.balda_game()
@bot.message_handler(func=lambda message: True, content_types=['text'])
def answ(message):
    tmp = lower(message.text)
    search = balda.word_search(tmp)
    letter = balda.get_letter()
    ans = 'Пока слово ' + search + '\n' + letter
    if search == 'done':
        balda.restart()
    bot.send_message(message.chat.id, ans)




if __name__ == '__main__':
    bot.polling(none_stop=True)
# Это для тренировку реквестов
# URL = 'https://api.telegram.org/bot' + token + '/'
#
# def get_updates():
#     url = URL + 'getUpdates'
#     req = requests.get(url)
#     dis = req.json()
#     print(dis)
#     print()
#     for di in dis['result']:
#         d = di['message']
#         text = d['text']
#         print(text) хдесь выведется текст за этот день, всеь от каждого пользователя
#
#
#
#
#
# def main():
#     get_updates()
#
#
#
# if __name__ == '__main__':
#     main()