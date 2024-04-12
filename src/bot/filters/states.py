from aiogram.dispatcher.filters.state import StatesGroup, State


class AuthUser(StatesGroup):
    get_email_address = State()
    get_password = State()
    

class BaseQuestions(StatesGroup):
    get_fio = State()
    get_birth_date = State()
    get_death_date = State()
    get_workplace = State()
    get_country = State()