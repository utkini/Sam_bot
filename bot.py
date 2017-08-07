import telebot
from telebot import types
import requests
import config
import data
import pars

token = config.token
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome = data.welcome(message)
    bot.reply_to(message,welcome)

@bot.message_handler(commands=['help'])
def helper(message):
    helpr = data.helper(message)
    bot.send_message(message.chat.id, helpr)

@bot.message_handler(commands=['game'])
def game_change(message):
    makup_game = types.ReplyKeyboardMarkup()
    makup_game.row('Балда-game', 'Акинатор-game')
    bot.send_message(message.chat.id,data.choose_game,reply_markup=makup_game)



@bot.message_handler(func=lambda message: True, content_types=['text'])
def ans(message):

    mess = pars.initial(message.text)
    bot.send_message(message.chat.id, mess)





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