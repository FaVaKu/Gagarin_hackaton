from aiogram import types
from aiogram.dispatcher import FSMContext

from src.bot.data.loader import bot, dp, logger
from src.bot.texts.user_texts import *
from src.bot.filters.states import BaseQuestions

@dp.callback_query_handler(text='create_new_page', state="*")
async def create_new_page(callback: types.CallbackQuery, state: FSMContext):
    await bot.send_message(
        chat_id=callback.from_user.id,
        text=get_name_text
    )
    
    await BaseQuestions.get_fio.set()
    

@dp.message_handler(state=BaseQuestions.get_fio, content_types=types.ContentType.TEXT)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    
    await bot.send_message(
        chat_id=message.from_user.id,
        text=get_birth_date_text
    )
    
    await BaseQuestions.get_birth_date.set()
    

@dp.message_handler(state=BaseQuestions.get_birth_date, content_types=types.ContentType.TEXT)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(birth=message.text)
    
    await bot.send_message(
        chat_id=message.from_user.id,
        text=get_death_date_text
    )
    
    await BaseQuestions.get_death_date.set()
    

@dp.message_handler(state=BaseQuestions.get_death_date, content_types=types.ContentType.TEXT)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    
    await bot.send_message(
        chat_id=message.from_user.id,
        text=get_workplace_text
    )
    
    await BaseQuestions.get_workplace.set()
    

@dp.message_handler(state=BaseQuestions.get_workplace, content_types=types.ContentType.TEXT)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    
    await bot.send_message(
        chat_id=message.from_user.id,
        text=get_country_text
    )
    
    await BaseQuestions.get_country.set()
    

@dp.message_handler(state=BaseQuestions.get_country, content_types=types.ContentType.TEXT)
async def get_name(message: types.Message, state: FSMContext):
    await state.finish()
    
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Отлично, дальше - больше'
    )
    