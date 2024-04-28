from aiogram.fsm.state import State, StatesGroup


class Restaurant(StatesGroup):
    restaurant = State()
    menu = State()
