# Продолжить разработку телеграмм бота. Добавить опции:
# -'Хочу гулять'
# -'Хочу спать'
# -'Хочу шутку'

import telebot
from telebot import types

token='5490345803:AAEKIRyTkE5SqOsQtU9nWUyXPbgBOJFgb8Q'
bot=telebot.TeleBot(token)

def create_keyboard(): #функция для создания кнопок
    keyboard = types.InlineKeyboardMarkup() #создаем пустую клавиатуру (виртуальную)
    drink_btn = types.InlineKeyboardButton(text='Хочу пить!', callback_data='1') #создаем конкретную кнопку на клавиатуру
    eat_btn = types.InlineKeyboardButton(text='Хочу есть!', callback_data='2')
    walk_btn = types.InlineKeyboardButton(text='Хочу гулять!', callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text='Хочу спать!', callback_data='4')
    joke_btn = types.InlineKeyboardButton(text='Хочу шутку!', callback_data='5')
    keyboard.add(drink_btn) #добавили кнопку на клавиатуру
    keyboard.add(eat_btn)
    keyboard.add(walk_btn)
    keyboard.add(sleep_btn)
    keyboard.add(joke_btn)
    return keyboard

@bot.message_handler(commands=['start']) #декоратор при перехвате команды start запустит функцию start_bot
def start_bot(message):
    keyword = create_keyboard()
    bot.send_message(
        message.chat.id,
        'Добрый день! Сделайте выбор!',
        reply_markup=keyword
    )

@bot.callback_query_handler(func=lambda call:True) #queary_handler перехватывает запросы
def callback(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data == '1':
            img = open('water.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo= img,
                caption='Картинка воды',
                reply_markup=keyboard
            )
        if call.data == '2':
            img = open('food.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка еды',
                reply_markup=keyboard
            )

        if call.data == '3':
            img = open('walk.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка аллеи',
                reply_markup=keyboard
            )

        if call.data == '4':
            img = open('sleep.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка сна',
                reply_markup=keyboard
            )

        if call.data == '5':
            img = open('joke.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка шутки',
                reply_markup=keyboard
            )


if __name__ == '__main__':
    bot.polling(none_stop=True) #включаем работу бота без остановок