from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from asyncpg import Pool
from logging import Logger
import asyncio
import asyncpg
import logging
import os
import time

from src.bot.data.config import *


async def create_db_pool() -> Pool:
    """ Create and return a connection pool.

    Returns:
        Pool: connection pool
    """
    return await asyncpg.create_pool(
        host=HOST_DB,
        user=LOGIN_DB,
        password=PASSWORD_DB,
        database=NAME_OF_DB,
    )

def get_logger() -> Logger:
    """ Set logger configuration

    Returns:
        Logger: logger
    """
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('apscheduler').setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s')
    handler = logging.FileHandler(
        os.path.join(
            os.getcwd(),
            'logs',
            f'{time.strftime("%Y_%m_%d-%H_%M_%S", time.localtime())}.log'
        ),
        mode='w',
        encoding='utf-8'
    )
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(handler)
    
    return root_logger


bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
logger = get_logger()
scheduler = AsyncIOScheduler()
#TODO: db_connection: Pool = asyncio.run(create_db_pool())