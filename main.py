import os, asyncio, re, time
from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

dp = Dispatcher()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)

@dp.message(CommandStart())
async def startup(message: Message):
    first_name = message.from_user.first_name
    await message.answer(f'Hello {first_name}')


async def news(message: Message):
    caption = f"Published on {time}\n\n{news_text}"
    await bot.send_photo(chat_id=image_url, photo=image_url, caption=caption)


@dp.message(lambda msg: msg.text == '/news')
async def send_news(message: Message):
    with (sync_playwright() as play):
        browser = play.firefox.find_all(class_='news-container')
        for article in browser:
            date_time = article.find(class_='date').text.strip()
            news_time = re.search(r'\d{2}:\d{2}', date_time).group(0)
            current_time = time.struct_time('%H:%M')
            if news_time == current_time:
                headline = article.find('a').text.strip()
                image_url = article.find('img')['src']
                await message.answer(image_url, date_time, headline)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())