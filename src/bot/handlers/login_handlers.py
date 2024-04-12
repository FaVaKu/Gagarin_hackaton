from aiogram import types
from aiogram.dispatcher import FSMContext

from src.bot.data.loader import bot, dp, logger
from src.bot.keyboards.user_keyboards import login_by_phone
from src.bot.texts.user_texts import *
from src.bot.filters.states import AuthUser
from src.bot.utils.tools import MemoryCode

@dp.message_handler(state=AuthUser.get_email_address, content_types=types.ContentType.TEXT, regexp=r'[\w.-]+@[\w.-]+(?:.[\w]+)+')
async def get_email_address(message: types.Message, state: FSMContext):
    
    await state.update_data(email_address=message.text)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Введите пароль:'
    )
    await AuthUser.get_password.set()

@dp.message_handler(state=AuthUser.get_email_address, content_types=types.ContentType.TEXT)
async def get_email_address_invalid(message: types.Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Вы ввели некорректную почту, повторите попытку:'
    )
    

@dp.message_handler(state=AuthUser.get_password, content_types=types.ContentType.TEXT)
async def get_email_address(message: types.Message, state: FSMContext):
    async with state.proxy() as state_data:
        email_address = state_data.get('email_address')
        password = message.text
        
    data = await MemoryCode.get_access_token(email=email_address, password=password)
    
    if access_token:=data.get('access_token'):
        await dp.conn.execute(
            'UPDATE users SET access_key = $1 WHERE tg_id = $2',
            access_token,
            message.from_user.id
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Неверный пароль, повтроите еще раз'
        )