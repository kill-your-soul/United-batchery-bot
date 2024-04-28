from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.main_keyboard import create_main_keyboard, menu_keyboard
from loguru import logger
from states.start import Restaurant
from utils.location import locations


async def command_start_handler(message: Message, state: FSMContext) -> None:
    keyboard = await create_main_keyboard()
    logger.debug(f"New user with username @{message.from_user.username}")
    await message.answer("Выберите ресторан", reply_markup=keyboard)
    await state.set_state(Restaurant.restaurant)


async def options_handler(message: Message, state: FSMContext) -> None:
    keyboard = await menu_keyboard()
    logger.debug(f"Пользователь выбрал {message.text}")
    await state.update_data(restaurant=message.text)
    await message.answer("Выберите далее", reply_markup=keyboard)
    await state.set_state(Restaurant.menu)


async def menu_handler(message: Message, state: FSMContext) -> None:
    logger.debug("Пользователь открыл меню")
    await message.answer("Меню")


async def geo_handler(message: Message, state: FSMContext) -> None:
    location = locations[(await state.get_data())["restaurant"]]
    await message.answer_location(latitude=location["latitude"], longitude=location["longitude"])
