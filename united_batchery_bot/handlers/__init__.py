from aiogram import F, Router
from aiogram.filters import CommandStart, StateFilter
from loguru import logger
from states.start import Restaurant

from . import start


@logger.catch()
def setup_handlers() -> Router:
    router = Router()
    router.message.register(start.command_start_handler, CommandStart())
    router.message.register(start.options_handler, StateFilter(Restaurant.restaurant))
    router.message.register(start.menu_handler, StateFilter(Restaurant.menu), F.text == "Меню")
    router.message.register(start.geo_handler, StateFilter(Restaurant.menu), F.text == "Построить маршрут")
    router.message.register(lambda x: x, StateFilter(Restaurant.menu), F.text == "Забронировать стол")
    router.message.register(lambda x: x, StateFilter(Restaurant.menu), F.text == "Заказать доставку")
    router.message.register(lambda x: x, StateFilter(Restaurant.menu), F.text == "Чат")
    return router
