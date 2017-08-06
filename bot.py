import telebot
import requests
import config
import data

token = config.token
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def ans(message):

    mess = data.initial(message.text)
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