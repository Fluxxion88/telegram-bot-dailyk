import os 
from dotenv import load_dotenv
import asyncio
import telegram


load_dotenv()
bot_token = os.getenv("TELEGRAM_BOT")


async def main():
    bot = telegram.Bot(bot_token)
    async with bot:
        await bot.send_message(text='Хлопья', chat_id=797248866)


if __name__ == '__main__':
    asyncio.run(main())