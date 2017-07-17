import config
import telebot
import parser
import data

bot = telebot.TeleBot(config.token);

@bot.message_handler(commands=['start'])
def answer(message):
    bot.send_message(message.chat.id, data.hello)

@bot.message_handler(commands=['help'])
def answer(message):
    bot.send_message(message.chat.id, data.helper)

@bot.message_handler(content_types = ["text"])
def repeat_all_messages(message):
    '''
    score = []
    score.append(message.text)
    if message.text == data.check:
        bot.send_message(message.chat.id, score)
    else:
        bot.send_message(message.chat.id, 'ok')
    '''
    bot.send_message(message.chat.id, parser.parse_message(message.text))
    if parser.parse_message(message.text) == True:
        bot.send_photo(message.chat.id, data.picture)
    else:
        bot.send_audio(message.chat.id, data.audio)

if __name__ == '__main__':
    bot.polling(none_stop = True)