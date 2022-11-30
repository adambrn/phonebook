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
    await message.answer('/help - все команды \n/all  - все записи \n/s техт - поиск ')

@dp.message_handler(commands=['all'])
async def process_help_command(message: types.Message):
    db_path = file_operations.get_db_path()
    data = db_get(db_path,'people')
    result = [f'{i[0]}. {i[1]} {i[2]} {i[3]} тел: {i[4]}' for i in data]
    await message.answer('\n'.join(map(str,result)))

@dp.message_handler(commands=['s'])
async def process_help_command(message: types.Message):
    search_result = []
    result = []
    db_path = file_operations.get_db_path()
    data = db_get(db_path,'people')
    text = ''
    try:
        text = message.text.split(maxsplit=1)[1]
        for record in data:
            if text.lower() in ''.join(str(record)).lower():   
                search_result.append(record)
            result = [f'{i[0]}. {i[1]} {i[2]} {i[3]} тел: {i[4]}' for i in search_result]
    except Exception:
        result += ('Введите текст для поиска после команды /s',)
    
    if not result: result += ('Ничего не найдено',)
    await message.answer('\n'.join(map(str,result)))

@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer('Напишите команду или /help для просмотра всех команд!')



if __name__ == '__main__':
    executor.start_polling(dp)