import telebot
from config import TOKEN
from telebot import TeleBot
from telebot import types

bot = TeleBot(TOKEN)

print('выполняется')
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/schedule')
    btn2 = types.KeyboardButton('/info')
    btn3 = types.KeyboardButton('/homework')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, """
Привет! Я - школьный бот помощник. Могу отправить тебе расписание по команде или сделать ещё что-то.
Выбери команду из меню
/schedule - расписание уроков
/info - информация по урокам
/homework - домашка
""",
    reply_markup=markup
        )
    print('Команда выполняется')
bot.infinity_polling()
