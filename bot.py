import telebot
from config import token  # из файла config.py забираем нашу переменную с токеном

# Создаем экземпляр бота
bot = telebot.TeleBot(token)


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Напиши мне что-нибудь )')


# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

# Задание 1
import random


@bot.message_handler(commands=["task_1"])
def task_1(message):
    bot.send_message(message.chat.id, 'Задание 1, случайное число: ' + str(random.randint(1, 10)))


# Запускаем бота
bot.polling(none_stop=True, interval=0)