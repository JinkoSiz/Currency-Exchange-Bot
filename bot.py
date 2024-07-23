from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import redis

API_TOKEN = 'api'
REDIS_HOST = 'redis'
REDIS_PORT = 6379

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@dp.message_handler(commands=['exchange'])
async def exchange(message: types.Message):
    try:
        _, from_currency, to_currency, amount = message.text.split()
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        amount = float(amount)
        if from_currency == "RUB":
            to_rate = float(r.get(to_currency))
            converted_amount = amount / to_rate
        elif to_currency == "RUB":
            from_rate = float(r.get(from_currency))
            converted_amount = from_rate * amount
        else:
            from_rate = float(r.get(from_currency))
            to_rate = float(r.get(to_currency))
            converted_amount = (from_rate / to_rate) * amount
        await message.reply(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except Exception as e:
        await message.reply(f"Ошибка при конвертации валют: {str(e)}")

@dp.message_handler(commands=['rates'])
async def rates(message: types.Message):
    keys = r.keys()
    rates = [f"{key}: {r.get(key)}" for key in keys]
    await message.reply("\n".join(rates))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
