from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.main_keyboard import create_main_keyboard, menu_keyboard
from loguru import logger
from states.start import Restaurant
from states.usermode import Booking
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

async def chat(message: Message, state: FSMContext) -> None:
    logger.debug("Пользователь открыл чаты")
    await message.answer("ссылки")

async def book_table_day(message: Message, state: FSMContext) -> None:
    logger.debug("Пользователь начал бронировать стол")
    await message.answer("Введите день:")
    await state.set_state(Booking.day)

async def book_table_time(message: Message, state: FSMContext) -> None:
    await state.update_data(day=message.text)
    await message.answer("Введите время:")
    await state.set_state(Booking.time)

async def book_table_guests(message: Message, state: FSMContext) -> None:
    await state.update_data(time=message.text)
    await message.answer("Введите количество гостей:")
    await state.set_state(Booking.amount_of_guests)

async def book_table_number(message: Message, state: FSMContext) -> None:
    await state.update_data(guests=message.text)
    await message.answer("Введите номер телефона:")
    await state.set_state(Booking.number)

async def book_table_end(message: Message, state: FSMContext) -> None:
    await state.update_data(number=message.text)
    info_booking = await state.get_data()
    await message.answer(text=str(info_booking))
    logger.debug(info_booking)
    await state.set_state(Restaurant.menu)
    await message.answer("Спасибо! Мы вам перезвоним для подтверждения брони.")

async def geo_handler(message: Message, state: FSMContext) -> None:
    location = locations[(await state.get_data())["restaurant"]]
    await message.answer_location(latitude=location["latitude"], longitude=location["longitude"])
