from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from src.bot.utils.bot_tools import get_admins_ids

# Проверка на админа
class IsAdmin(BoundFilter):
    async def check(self, message: Message):
        if message.from_user.id in await get_admins_ids():
            return True
        
        return False
    
# Проверка на не админа
class IsNotAdmin(BoundFilter):
    async def check(self, message: Message):
        if message.from_user.id in await get_admins_ids():
            return False
        
        return True