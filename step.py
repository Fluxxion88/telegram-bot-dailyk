import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
import dotenv
from sqlalchemy import Column, BigInteger, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    telegram_id = Column(BigInteger, primary_key=True)
    name = Column(Text)
    created_at = Column(DateTime)

class Habit(Base):
    __tablename__ = "habits"
    id = Column(BigInteger, primary_key=True)
    telegram_id = Column(BigInteger, ForeignKey("users.telegram_id"))
    name = Column(Text)
    description = Column(Text)
    times_a_day = Column(Integer)

class Completion(Base):
    __tablename__ = "completions"
    id = Column(BigInteger, primary_key=True)
    habit_id = Column(BigInteger, ForeignKey("habits.id"))
    completed_at = Column(DateTime)





dotenv.load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): #? чё за контекст? что за вводные
    await context.bot.send_message(                                     #? что тут делает await? типо чё он делает
        chat_id=update.effective_chat.id, 
        text="I'm a bot, please talk to me!"
    )

async def help(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Нет, целуй попу"
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)
    
    application.run_polling()