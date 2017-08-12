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

def seporate(text):
    try:
        tmp = text[len(text)-1]
        return tmp
    except IndexError:
        return 'Ooops'


balda = search_word.balda_game()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome = data.welcome(message)
    bot.send_message(message.chat.id,welcome)

@bot.message_handler(commands=['help'])
def helper(message):
    helpr = data.helper(message)
    bot.send_message(message.chat.id, helpr)

@bot.message_handler(regexp='[Кк]акое слово')
def answer(message):
    bot.send_message(message.chat.id,balda.get_word())

@bot.message_handler(regexp='[Зз]аного')
def answer(message):
    balda.restart()
    bot.send_message(message.chat.id,'Хорошо, давай начнем сначала')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def answ(message):
    tmp = lower(message.text)
    tmp = seporate(tmp)
    if tmp == 'Ooops':
        bot.send_message(message.chat.id,'Дружище, что-то пошло не так... Введи пожалуйста букву или слово еще разок')
    search = balda.word_search(tmp)
    letter = balda.get_letter()
    ans = letter + '\n' + data.middle_comment_ans() + '\n' + search
    if search == 'done':
        balda.restart()
        if balda.f == True:
            bot.send_message(message.chat.id,'Ну вот я и победил. Давай еще раз! Говори букву')
        else:
            bot.send_message(message.chat.id, 'Я.. проиграл... Нужно срочно отыграться! Говори букву')
    elif search == 'There is no such word':
        bot.send_message(message.chat.id, 'Я не знаю такого слова... Давай ты скажешь букву заного')
    else:
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