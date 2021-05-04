import telebot
from telebot import types

bot = telebot.TeleBot('1770476779:AAEsupFUhVx8SM6Mh-gJ4Ri5AAC7_yJQvFU')

# Ответы или действия на текстовые команды
@bot.message_handler(content_types=['text'])
def get_text_massage(massage):
    if massage.text == 'Старт' or massage.text == 'старт':
        # Клавиатура
        keyboard = types.InlineKeyboardMarkup()
        key_reboot = types.InlineKeyboardButton(text='1. Перезапуск сервера', callback_data='reboot')
        key_kick = types.InlineKeyboardButton(text='2. Выгнать пользователей', callback_data='kick')
        key_service = types.InlineKeyboardButton(text='3. Перезапуск службы Агент 1С', callback_data='service')
        keyboard.add(key_reboot)
        keyboard.add(key_kick)
        keyboard.add(key_service)
        # Клавиатура конец

        bot.send_message(massage.from_user.id, 'Доступные команды:', reply_markup=keyboard)
        bot.send_message(massage.from_user.id, 'Список доступных команд будет пополняться =)')
    else:
        bot.send_message(massage.from_user.id, 'Неизвестная команда...(')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'reboot':
        bot.send_message(call.message.chat.id, 'Перезапускаю сервер....')
    elif call.data == 'service':
        bot.send_message(call.message.chat.id, 'Перезапускаю службу....')
    elif call.data == 'kick':
        keyboard_baz = types.InlineKeyboardMarkup()
        first_baze = types.InlineKeyboardButton(text='1. Первая база', callback_data='first_baze')
        second_baze = types.InlineKeyboardButton(text='2. Вторая база', callback_data='second_baze')
        third_baze = types.InlineKeyboardButton(text='3. Третья база', callback_data='third_baze')
        keyboard_baz.add(first_baze)
        keyboard_baz.add(second_baze)
        keyboard_baz.add(third_baze)
        bot.send_message(call.message.chat.id, 'Выберите базу из списка:', reply_markup=keyboard_baz)

# Запуск бота на ожидание сообщений
bot.polling(none_stop=True, interval=0)
