from dotenv import load_dotenv
from typing import List
import os


if not load_dotenv():
    raise Exception("Невозможно прогрузить .env файл. Возможно, он находится не в той директории")

DEVELOPER_ID: int = int(os.getenv("DEVELOPER_ID"))
ADMINS_IDS: List[int] = list(map(int, os.getenv("ADMINS_IDS").replace(' ', '').split(',')))
BOT_TOKEN: str = os.getenv("BOT_TOKEN")

HOST_DB: str = os.getenv("HOST_DB")
LOGIN_DB: str = os.getenv("LOGIN_DB")
PASSWORD_DB: str = os.getenv("PASSWORD_DB")
NAME_OF_DB: str = os.getenv("NAME_OF_DB")


