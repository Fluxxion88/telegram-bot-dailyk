from bot.handlers import start, help_command, add_habit_command, list_habits_command, delete_habit_command, done_command, streak_command
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
import dotenv
from db.models import Base
from db.connection import engine

dotenv.load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    Base.metadata.create_all(engine)

    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    help_handler = CommandHandler('help', help_command)
    application.add_handler(help_handler)
    
    add_habit_handler = CommandHandler('add', add_habit_command)
    application.add_handler(add_habit_handler)
    
    list_handler = CommandHandler('list', list_habits_command)
    application.add_handler(list_handler)
    
    delete_habit_handler = CommandHandler('delete', delete_habit_command)
    application.add_handler(delete_habit_handler)
    
    done_handler = CommandHandler('done', done_command)
    application.add_handler(done_handler)
    
    streak_handler = CommandHandler('streak', streak_command)
    application.add_handler(streak_handler)
    
    application.run_polling()