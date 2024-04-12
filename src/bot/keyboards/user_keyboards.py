from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
import calendar

login_by_phone = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text='Отправить номер телефона', request_contact=True)
)


main_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Создать страницу', callback_data='create_new_page')
).add(
    InlineKeyboardButton(text='Мои страницы', callback_data='my_pages')
).add(
    InlineKeyboardButton(text='Помощь', callback_data='help')
)