import telebot
import os
from telebot import types
from dotenv import load_dotenv

load_dotenv('token.env')

TELEGRAM_BOT_TOKEN = os.getenv('BOTTOKEN')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        keyboard = types.InlineKeyboardMarkup()
        button_github = types.InlineKeyboardButton(text='Страница GitHub', callback_data='github')
        button_projects = types.InlineKeyboardButton(text='Проекты', callback_data='projects')
        keyboard.add(button_github, button_projects)
        bot.send_message(message.from_user.id, 'Привет! Что ты хочешь сделать?', reply_markup=keyboard)


def projects(message):
    if message.text == '/projects':
        keyboard = types.InlineKeyboardMarkup()
        button_link = types.InlineKeyboardButton(text='MonotonDev_BOT', callback_data='projects-monotondev_bot')
        button_github = types.InlineKeyboardButton(text='Страница GitHub', callback_data='github')
        button_back = types.InlineKeyboardButton(text='Вернуться в меню', callback_data='back-to-menu')
        keyboard.add(button_link, button_github, button_back)
        bot.send_message(message.from_user.id, 'Выбери интерисующий проект и нажми на кнопку с ним.',
                         reply_markup=keyboard)


def github(message):
    if message.text == '/github':
        keyboard = types.InlineKeyboardMarkup()
        button_link = types.InlineKeyboardButton(text='Страница GitHub', callback_data='github-link')
        button_back = types.InlineKeyboardButton(text='Вернуться в меню', callback_data='back-to-menu')
        keyboard.add(button_link, button_back)
        bot.send_message(message.from_user.id, 'Чтобы получить ссылку на GitHub нажми на соответсвующую кнопку ниже.',
                         reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'projects':
        keyboard = types.InlineKeyboardMarkup()
        button_link = types.InlineKeyboardButton(text='MonotonDev_BOT', callback_data='projects-monotondev_bot')
        button_github = types.InlineKeyboardButton(text='Страница GitHub', callback_data='github')
        button_back = types.InlineKeyboardButton(text='Вернуться в меню', callback_data='back-to-menu')
        keyboard.add(button_link, button_github, button_back)
        bot.send_message(call.message.chat.id, 'Выбери интерисующий проект и нажми на кнопку с ним.',
                         reply_markup=keyboard)
    elif call.data == 'github':
        keyboard = types.InlineKeyboardMarkup()
        button_link = types.InlineKeyboardButton(text='Страница GitHub', callback_data='github-link')
        button_back = types.InlineKeyboardButton(text='Вернуться в меню', callback_data='back-to-menu')
        keyboard.add(button_link, button_back)
        bot.send_message(call.message.chat.id, 'Чтобы получить ссылку на GitHub нажми на соответсвующую кнопку ниже.',
                         reply_markup=keyboard)
    elif call.data == 'back-to-menu':
        keyboard = types.InlineKeyboardMarkup()
        button_github = types.InlineKeyboardButton(text='Страница GitHub', callback_data='github')
        button_projects = types.InlineKeyboardButton(text='Проекты', callback_data='projects')
        keyboard.add(button_github, button_projects)
        bot.send_message(call.message.chat.id, 'Привет! Что ты хочешь сделать?', reply_markup=keyboard)
    elif call.data == 'github-link':
        bot.send_message(call.message.chat.id, 'GitHub - https://github.com/MonotonB')

    elif call.data == 'projects-monotondev_bot':
        bot.send_message(call.message.chat.id, 'MonotonDev_BOT - https://github.com/MonotonB/MonotonDev_BOT')
        keyboard = types.InlineKeyboardMarkup()
        button_link = types.InlineKeyboardButton(text='MonotonDev_BOT', callback_data='projects-monotondev_bot')
        button_github = types.InlineKeyboardButton(text='Страница GitHub', callback_data='github')
        button_back = types.InlineKeyboardButton(text='Вернуться в меню', callback_data='back-to-menu')
        keyboard.add(button_link, button_github, button_back)
        bot.send_message(call.message.chat.id, 'Выбери интерисующий проект и нажми на кнопку с ним.',
                         reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)
