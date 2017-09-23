import telebot
from sam_bot.data import search_word
from sam_bot.data import data
from sam_bot.data import config
from sam_bot.data import check_word

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


balda = search_word.BaldaGame()
session_balda = check_word.UserWord()


# Обрабатываем команду /start и выводим приветствие для пользователя, обращаеся к нему по имени
@bot.message_handler(commands=['start'])
def starter(message):
    welcome = data.welcome(message)
    session_balda.create_new_user(message.chat.username, message.chat.id)  # Создаем пользователя в БД
    bot.send_message(message.chat.id, welcome)


# Обрабатываем команду /help  и выводим правила игры с некоторыми подсказками или словами помощниками,
# если игра очень сложная.
@bot.message_handler(commands=['help'])
def support(message):
    helper = data.helper()
    bot.send_message(message.chat.id, helper)


# Команда для админа, иказывает сколько пользователей играло в игру балда
#
# !!!!Написать декоратор для проверки на админа!!!!
#
@bot.message_handler(commands=['users'])
def how_users(message):
    count = session_balda.how_users()
    ans = 'Количество людей, которые играли со мной: ' + str(count)
    bot.send_message(message.chat.id, ans)


# Первый обработчик подсказки. Если игрок не знает слово, он может спросить бота и отталкиваться от этого
# в дальнейшем
@bot.message_handler(regexp='[Кк]акое слово')
def how_word(message):
    word = session_balda.get_word_bot(message.chat.username, message.chat.id)
    # нужно заменить word на balda.get_word() для того, чтобы работала вторая БД
    ans = 'Я загадал слово:\n' + word
    bot.send_message(message.chat.id, ans)


# Второй обработчик подсказки Если игрок хочет начать сначала, он в любой момент может сказать боту заново
# и проболжить играть
@bot.message_handler(regexp='[Зз]аново')
def again(message):
    balda.restart()
    session_balda.restart(message.chat.username, message.chat.id)
    bot.send_message(message.chat.id, 'Хорошо, давай начнем сначала')


# Основная функция, которая берет все сообщения, если они дошли до нее и обрабатывает.
# Тело функции проверяет пришедшее сообщение на корректность и превращает его в нужый вид для класса балда,
# который и есть ядро программы.
# В зависимости от полученных данных от класса уже можно производить оценку и выбирать по какому сценарию игры
# отвечать
@bot.message_handler(func=lambda message: True, content_types=['text'])
def answer_balda(message):
    if session_balda.user_check(message.chat.username, message.chat.id):
        tmp = lower(message.text)
        tmp = sepаr(tmp)  # Нужно написать проверку на букву а не на цифру и не на число и на корректность ввода
        if tmp == 'Ooops':
            bot.send_message(message.chat.id, 'Дружище, что-то пошло не так...'
                                              ' Введи пожалуйста букву или слово еще разок')
        else:
            # Эта команда присваивает переменной экземпляра  значение, которое принадлежит этому пользователю
            balda.word = session_balda.get_word(message.chat.username, message.chat.id)

            search = balda.word_search(tmp)
            letter = balda.get_letter()
            ans = letter + '\n' + data.middle_comment_ans() + '\n' + search
            if search == 'done':
                balda.restart()
                an = balda.get_word()
                if balda.f == True:
                    win_ans = 'У нас получилось слово:\n' + an + '\nИ получается, что это раунд за мной!\n'
                    session_balda.restart(message.chat.username, message.chat.id)
                    bot.send_message(message.chat.id, win_ans + 'Давай еще раз! Говори букву')
                else:
                    lose_ans = 'Ну вот и все... Я говорю букву: ' + an[len(an) - 1] + '\n' + \
                               'И у нас получается слово\n' + an
                    session_balda.restart(message.chat.username, message.chat.id)
                    bot.send_message(message.chat.id, lose_ans +
                                     '\nЯ проиграл... Нужно срочно отыграться! Говори букву')
            elif search == 'There is no such word':
                bot.send_message(message.chat.id, 'Я не знаю такого слова... Давай ты скажешь букву заново')
            else:
                # Вносит данную игру в БД сессий
                session_balda.set_word(message.chat.username, message.chat.id, search)
                session_balda.set_word_bot(message.chat.username, message.chat.id, balda.how_word)

                bot.send_message(message.chat.id, ans)
    else:
        bot.send_message(message.chat.id, "Что-то произошло, давай ты напишешь /start и попробуем еще разок?")


if __name__ == '__main__':
    bot.polling(none_stop=True)
