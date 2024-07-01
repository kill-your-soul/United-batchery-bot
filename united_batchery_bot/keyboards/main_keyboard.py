from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardMarkup,
    ReplyKeyboardBuilder,
    ReplyKeyboardMarkup,
)


async def create_main_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Восстания, 26").button(text="Просвещения, 46").button(text="Европейский, 21").button(
        text="Героев, 31"  # noqa: COM812
    )
    builder.adjust(2, 2)
    return builder.as_markup(one_time_keyboard=True, resize_keyboard=True)


async def menu_keyboard(url: str) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Меню", web_app=WebAppInfo(url=url)).button(
        text="Построить маршрут"
    ).button(text="Забронировать стол").button(
        text="Заказать доставку", web_app=WebAppInfo(url="https://unitedbutchers.delivery/"),
    ).button(text="Чат")
    builder.adjust(2, 2, 1)
    return builder.as_markup(one_time_keyboard=True, resize_keyboard=True)


async def keyboard_for_vosstania(url: str) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Меню", web_app=WebAppInfo(url=url)).button(
        text="Построить маршрут"
    ).button(text="Забронировать стол").button(
        text="Заказать доставку", web_app=WebAppInfo(url="https://unitedbutchers.delivery/"),
    )
    builder.adjust(2, 2)
    return builder.as_markup(one_time_keyboard=True, resize_keyboard=True)