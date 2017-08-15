import telebot
from sam_bot.data import search_word
from sam_bot.data import data
from sam_bot.data import config


token = config.token
bot = telebot.TeleBot(token)


def lower(text):
    return text.lower()


def sepаr(text):
    try:
        for c in text:
            if ord(c) < 1040 or ord(c) > 1103:
                return 'Ooops'
        tmp = text[len(text) - 1]
        return tmp
    except Exception:
        return 'Ooops'


balda = search_word.balda_game()

#Обрабатываем команду /start и выводим приветствие для пользователя, обращаеся к нему по имени
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome = data.welcome(message)
    bot.send_message(message.chat.id, welcome)


# Обрабатываем команду /help  и выводим правила игры с некоторыми подсказками или словами помощниками,
# если игра очень сложная.
@bot.message_handler(commands=['help'])
def helper(message):
    helpr = data.helper(message)
    bot.send_message(message.chat.id, helpr)


# Первый обработчик подсказки. Если игрок не знает слово, он может спросить бота и отталкиваться от этого
# в дальнейшем
@bot.message_handler(regexp='[Кк]акое слово')
def answer(message):
    bot.send_message(message.chat.id, balda.get_word())


# Второй обработчик подсказки Если игрок хочет начать сначала, он в любой момент может сказать боту заново
# и проболжить играть
@bot.message_handler(regexp='[Зз]аново')
def answer(message):
    balda.restart()
    bot.send_message(message.chat.id, 'Хорошо, давай начнем сначала')

# Основная функция, которая берет все сообщения, если они дошли до нее и обрабатывает.
# Тело функции проверяет пришедшее сообщение на корректность и превращает его в нужый вид для класса балда,
# который и есть ядро программы.
# В зависимости от полученных данных от класса уже можно производить оценку и выбирать по какому сценарию игры
# отвечать
@bot.message_handler(func=lambda message: True, content_types=['text'])
def answ(message):
    tmp = lower(message.text)
    tmp = sepаr(tmp)  # Нужно написать проверку на букву а не на цифру и не на число и на корректность ввода
    if tmp == 'Ooops':
        bot.send_message(message.chat.id, 'Дружище, что-то пошло не так...'
                                          ' Введи пожалуйста букву или слово еще разок')
    else:
        search = balda.word_search(tmp)
        letter = balda.get_letter()
        ans = letter + '\n' + data.middle_comment_ans() + '\n' + search
        if search == 'done':
            balda.restart()
            if balda.f == True:
                bot.send_message(message.chat.id, 'Ну вот я и победил. Давай еще раз! Говори букву')
            else:
                bot.send_message(message.chat.id, 'Я.. проиграл... Нужно срочно отыграться! Говори букву')
        elif search == 'There is no such word':
            bot.send_message(message.chat.id, 'Я не знаю такого слова... Давай ты скажешь букву заного')
        else:
            bot.send_message(message.chat.id, ans)


if __name__ == '__main__':
    bot.polling(none_stop=True)
