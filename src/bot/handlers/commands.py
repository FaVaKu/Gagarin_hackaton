from aiogram import types
from aiogram.dispatcher import FSMContext
from datetime import datetime, timezone

from src.bot.data.loader import bot, dp, logger
from src.bot.filters.states import AuthUser
from src.bot.keyboards.user_keyboards import main_keyboard
from src.bot.texts.user_texts import *


@dp.message_handler(state='*', commands=["start", "cancel"])
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    
    user_data = await dp.conn.fetchrow('SELECT * FROM users WHERE tg_id = $1', message.from_user.id)
    
    if not user_data:
        await dp.conn.execute(
            'INSERT INTO users (tg_id, username, first_name, last_name, date_of_join) VALUES ($1, $2, $3, $4, $5)',
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
            datetime.now(timezone.utc)
        )
    else:
        await dp.conn.execute(
            'UPDATE users SET is_bot_blocked = False WHERE tg_id = $1',
            message.from_user.id
        )
        
    if user_data and not user_data['access_key']:
        await AuthUser.get_email_address.set()
        
        await bot.send_message(
            chat_id=message.from_user.id,
            text=login_text,
            disable_web_page_preview=True
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=main_text,
            reply_markup=main_keyboard
        )

