from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from core.config import settings
from keyboards.main_keyboard import create_main_keyboard, keyboard_for_end, keyboard_for_vosstania, menu_keyboard
from loguru import logger
from states.start import Restaurant
from states.usermode import Booking
from utils.location import locations


async def command_start_handler(message: Message, state: FSMContext) -> None:
    keyboard = await create_main_keyboard()
    logger.debug(f"New user with username @{message.from_user.username}")
    await message.answer(
        "Добро пожаловать в мясной ресторан со своей пивоварней United Butchers! Чтобы продолжить, выберите пожалуйста адрес ресторана, который вы собираетесь посетить!",
        reply_markup=keyboard,
    )
    await state.set_state(Restaurant.restaurant)


async def options_handler(message: Message, state: FSMContext) -> None:
    # keyboard = await menu_keyboard()
    if message.text == "Просвещения, 46":
        keyboard = await menu_keyboard(settings.DOMAIN + "/vosstania")
    if message.text == "Европейский, 21":
        keyboard = await menu_keyboard(settings.DOMAIN + "/vosstania")
    if message.text == "Героев, 31":
        keyboard = await menu_keyboard(settings.DOMAIN + "/")
    if message.text == "Восстания, 26":
        keyboard = await keyboard_for_vosstania(settings.DOMAIN + "/vosstania")
    logger.debug(f"Пользователь выбрал {message.text}")
    await state.update_data(restaurant=message.text)
    await message.answer("Выберите, пожалуйста, вопрос, который вас интересует.", reply_markup=keyboard)
    await state.set_state(Restaurant.menu)


async def menu_handler(message: Message, state: FSMContext) -> None:
    logger.debug("Пользователь открыл меню")
    await message.answer("Меню")


async def chat(message: Message, state: FSMContext) -> None:
    logger.debug("Пользователь открыл чаты")
    if (await state.get_data())["restaurant"] == "Просвещения, 46":
        await message.answer("https://t.me/+8i33QxklO1c5ZWFi")
    elif (await state.get_data())["restaurant"] == "Европейский, 21":
        await message.answer("https://t.me/+s0ZBKNHThoNkMTUy")
    elif (await state.get_data())["restaurant"] == "Героев, 31":
        await message.answer("https://t.me/unitedbutchers_geroev")
    # await message.answer("ссылки")


async def book_table_day(message: Message, state: FSMContext) -> None:
    logger.debug("Пользователь начал бронировать стол")
    await message.answer("Введите день, в который вы планируете посетить ресторан")
    await state.set_state(Booking.day)


async def book_table_time(message: Message, state: FSMContext) -> None:
    await state.update_data(day=message.text)
    await message.answer("Введите время посещения")
    await state.set_state(Booking.time)


async def book_table_guests(message: Message, state: FSMContext) -> None:
    await state.update_data(time=message.text)
    await message.answer("Введите количество гостей")
    await state.set_state(Booking.amount_of_guests)


async def book_table_number(message: Message, state: FSMContext) -> None:
    await state.update_data(guests=message.text)
    await message.answer("Введите ваше имя и контактный номер для связи")
    await state.set_state(Booking.number)


async def book_table_end(message: Message, state: FSMContext) -> None:
    await state.update_data(number=message.text)
    info_booking = await state.get_data()
    # await message.answer(text=str(info_booking))
    answer = f"Новая заявка\n\nДень: {info_booking['day']}\nВремя: {info_booking['time']}\nКоличество гостей: {info_booking['guests']}\nНомер: {info_booking['number']}"  # noqa: E501
    if info_booking["restaurant"] == "Просвещения, 46":
        await message.bot.send_message(
            -1001687001589,
            answer,
        )
    elif info_booking["restaurant"] == "Европейский, 21":
        await message.bot.send_message(
            -1001854938336,
            answer,
        )
    elif info_booking["restaurant"] == "Героев, 31":
        await message.bot.send_message(
            -1002141952251,
            answer,
        )
    else:
        await message.bot.send_message(
            -1001524583162,
            answer,
        )
    logger.debug(info_booking)
    await state.set_state(Restaurant.menu)
    keyboard = await keyboard_for_end()
    await message.answer(
        "Спасибо за оставленную заявку, наш менеджер перезвонит вам в ближайшее время для подтверждения брони!\n\n До встречи",  # noqa: E501
        reply_markup=keyboard,
    )


async def geo_handler(message: Message, state: FSMContext) -> None:
    location = locations[(await state.get_data())["restaurant"]]
    await message.answer("Ждем вас в гостях по адресу")
    await message.answer_location(latitude=location["latitude"], longitude=location["longitude"])

async def end(message: Message, state: FSMContext) -> None:
    await command_start_handler(message, state)
