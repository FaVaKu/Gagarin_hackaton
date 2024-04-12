from aiogram import Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from asyncpg import Pool
from typing import List

from src.bot.data.config import ADMINS_IDS, DEVELOPER_ID, LOGIN_DB
from src.bot.data.loader import bot, logger, create_db_pool


async def on_startup(dp: Dispatcher):
    """ Функция, срабатывающая при запуске бота

    Args:
        dp (Dispatcher): Bot dispatcher
    """
    logger.info('Бот запущен')
    await set_bot_commands()
    
    dp.conn: Pool = await create_db_pool()
    
    await set_db(dp)
    
    await send_message_to_admins(text='✅ Бот запущен')
    

async def on_shutdown(dp: Dispatcher):
    """ Функция, срабатывающая при выключении бота

    Args:
        dp (Dispatcher): Bot dispatcher
    """
    logger.info('Бот остановлен')
    
    await send_message_to_admins(text='❌ Бот остановлен')
        

async def get_admins_ids() -> List[int]:
    """ Получает список ID всех админов

    Returns:
        List[int]: Список ID админов
    """
    return [DEVELOPER_ID] + ADMINS_IDS


async def send_message_to_admins(*, text: str = 'Тестовое сообщение', **kwargs):
    """ Отправляет сообщение админам

    Args:
        text (str, optional): Сообщение для отправки. Не может быть пустым. Defaults to 'Тестовое сообщение'.
    """
    assert text, 'Сообщение должно содержать хотя бы один символ'
    
    for ADMIN_ID in await get_admins_ids():
        try:
            await bot.send_message(
                chat_id=ADMIN_ID,
                text=text,
                **kwargs
            )
        except:
            continue

async def set_bot_commands():
    """ Ставит удобное меню команд для пользователя
    """
    # Команды для юзеров
    user_commands = [
        BotCommand("start", "📣 Главное меню"),
        BotCommand("about_bot", "🧑‍💻 Команда разработчиков"),
    ]

    # Команды для админов
    admin_commands = [
        BotCommand("start", "📣 Главное меню"),
        BotCommand("admin", "🛡️ Админ-меню"),
        BotCommand("about_bot", "🧑‍💻 Команда разработчиков"),
    ]
    
    await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())

    for admin_id in await get_admins_ids():
        try:
            await bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=admin_id))
        except:
            continue



async def set_db(dp):
    request = f"""
CREATE TABLE IF NOT EXISTS users
(
    tg_id bigint NOT NULL,
    first_name character varying,
    last_name character varying,
    username character varying,
    access_key character varying,
    is_bot_blocked boolean NOT NULL DEFAULT false,
    date_of_join timestamp with time zone,
    CONSTRAINT users_pkey PRIMARY KEY (tg_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS users
    OWNER to {LOGIN_DB};    
"""

    
    await dp.conn.execute(request)