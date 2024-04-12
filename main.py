# -*- coding: utf-8 -*-
from aiogram import executor

from src.bot.handlers import dp
from src.bot.utils.bot_tools import on_shutdown, on_startup


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)

