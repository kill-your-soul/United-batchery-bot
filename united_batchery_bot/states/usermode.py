from aiogram.fsm.state import State, StatesGroup


class Booking(StatesGroup):
    day = State()
    time = State()
    amount_of_guests = State()
    number = State()