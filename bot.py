from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from bot_config import TOKEN
from db_sqlite import db_get
import file_operations

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Телефонная книга\nНапишите команду или /help для просмотра всех команд!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer('/help - все команды \n/all  - все записи \n/search техт - поиск ')

@dp.message_handler(commands=['all'])
async def process_help_command(message: types.Message):
    db_path = file_operations.get_db_path()
    result = db_get(db_path,'people')
    await message.answer(*result)


@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer('Напишите команду или /help для просмотра всех команд!')



if __name__ == '__main__':
    executor.start_polling(dp)