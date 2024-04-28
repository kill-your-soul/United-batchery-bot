import asyncio
import logging
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import Redis, RedisStorage
from core.config import settings
from loguru import logger
import handlers

def setup_handlers(dp: Dispatcher) -> None:
    dp.include_router(handlers.setup_handlers())



class InterceptHandler(logging.Handler):
    def emit(self, record) -> None:
        level = logger.level(record.levelname).name
        logger.log(level, record.getMessage())


@logger.catch
async def main() -> None:
    logging.getLogger("aiogram").setLevel(logging.DEBUG)
    logging.getLogger("aiogram").addHandler(InterceptHandler())
    logging.getLogger("asyncio").setLevel(logging.DEBUG)
    logging.getLogger("asyncio").addHandler(InterceptHandler())
    base_dir = Path(__file__).resolve().parent.parent
    logger.add(base_dir / "logs.log", level="DEBUG")

    # client = MongoClient("mongodb://mongodb:27017")

    # logger.add(client.room_616.logs, level="INFO")
    bot = Bot(settings.TOKEN)
    redis = Redis(host=settings.REDIS_URI)
    storage = RedisStorage(redis)
    dp = Dispatcher(storage=storage)
    logger.info("Setup handlers")
    setup_handlers(dp)
    logger.info("Bot started")
    await dp.start_polling(bot)
    logger.info("Bot stoped")


if __name__ == "__main__":
    with logger.catch():
        asyncio.run(main())
