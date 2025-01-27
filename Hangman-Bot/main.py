import asyncio
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher, executor, types
from db import db_start, get_users_with_daily_option, add_daily_word, get_data
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN_API
from background import keep_alive
from hangman import get_daily_word  # Assuming get_daily_word is in hangman.py
import os


# Setting
my_timezone = pytz.timezone('Asia/Kolkata')
loop = asyncio.new_event_loop()
bot: Bot = Bot(TOKEN_API, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

# DAILY FUNCTION
async def daily_word_handler(user_id):
    new_daily_word = get_daily_word()
    if new_daily_word:  # Only proceed if a word was successfully retrieved
        await add_daily_word(new_daily_word)
        language = get_data(user_id, 4)
        keyboard = InlineKeyboardMarkup().add(
            InlineKeyboardButton('Yes ✅', callback_data='GuessNow'),
            InlineKeyboardButton('No ❌', callback_data='GuessLater')
        )

        if language == 'ua':
            await bot.send_message(chat_id=user_id, text="""👋 <b>Greetings!</b>
                
📆 Today's word is ready for <b>Тебе</b>. Do you want to guess it now? 🤔 Or you can save this opportunity until tomorrow! 🌄""",
                                   reply_markup=keyboard)
        elif language == 'gb':
            await bot.send_message(chat_id=user_id, text="""👋 <b>Hello!</b>

📆 Today the word is ready for <b>You</b>. Do you want to know the word now? 🤔 Or you can save your ability until tomorrow! 🌄""",
                                   reply_markup=keyboard)
    else:
        # Optionally, you could notify the user that there was an issue retrieving the word
        await bot.send_message(chat_id=user_id, text="Oops! There was an issue fetching today's word. Please try again later.")


async def send_daily_message():
    users = await get_users_with_daily_option()
    for user_id in users:
        await daily_word_handler(user_id)


async def on_start_up(_):
    await db_start()
    print('The bot was successfully launched!')


if __name__ == "__main__":
    from handlers import dp
    keep_alive()
    
    # Scheduler setup to send daily messages
    scheduler = AsyncIOScheduler(timezone=my_timezone)
    scheduler.add_job(send_daily_message, 'cron', hour=12, minute=30)    
    scheduler.start()
    
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)