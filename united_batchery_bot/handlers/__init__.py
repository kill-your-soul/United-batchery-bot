from aiogram import F, Router
from aiogram.filters import CommandStart, StateFilter
from loguru import logger
from states.start import Restaurant
from states.usermode import Booking

from . import start


@logger.catch()
def setup_handlers() -> Router:
    router = Router()
    router.message.register(start.command_start_handler, CommandStart())
    router.message.register(start.options_handler, StateFilter(Restaurant.restaurant))
    router.message.register(start.menu_handler, StateFilter(Restaurant.menu), F.text == "Меню")
    router.message.register(start.geo_handler, StateFilter(Restaurant.menu), F.text == "Построить маршрут")
    router.message.register(start.book_table_day, StateFilter(Restaurant.menu), F.text == "Забронировать стол")
    router.message.register(start.book_table_time, StateFilter(Booking.day), F.text)
    router.message.register(start.book_table_guests, StateFilter(Booking.time), F.text)
    router.message.register(start.book_table_number, StateFilter(Booking.amount_of_guests), F.text)
    router.message.register(start.book_table_end, StateFilter(Booking.number), F.text)
    router.message.register(start.chat, StateFilter(Restaurant.menu), F.text == "Чат")
    router.message.register(start.end, F.text == "В начало")
    return router
