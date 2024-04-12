from aiogram import types
from aiogram.dispatcher import FSMContext

from src.bot.data.loader import bot, dp, logger
from src.bot.filters.states import BaseQuestions
from src.bot.texts.user_texts import *

@dp.callback_query_handler(text='help', state="*")
async def create_new_page(callback: types.CallbackQuery, state: FSMContext):
    await bot.send_message(
        chat_id=callback.from_user.id,
        text=help_text
    )
    
