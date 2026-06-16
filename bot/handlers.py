from telegram import Update
from telegram.ext import ContextTypes
from db.repository import add_user, get_user, add_habit, get_habit_by_name, get_habits, delete_habit, get_habit_by_id, add_completion, count_completions
from db.connection import SessionLocal

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session = SessionLocal()
    try:
        name = update.effective_user.first_name
        if not get_user(session, update.effective_user.id):
            add_user(session, update.effective_user.id, update.effective_user.first_name )
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hi {name}, Im bot-tracker, I will help you with tracking your habits!"
        )
    finally:
        session.close()

async def help_command(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="""Available commands:
/add <name> - adds a new habit
/list - shows a list of all your habits
/done <id> - marks a habit as completed
/delete <id> - deletes a habit
/streak <id> - shows the streak""")

async def add_habit_command(update, context):
    session = SessionLocal()
    try:
        text_name = " ".join(context.args)
        user_id = update.effective_user.id
        if not text_name:
            await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text="Please write the command in full: /add <habit-name>"
        )
        elif get_habit_by_name(session, user_id, text_name):
            await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text="You already have this habit."
            )
        else:
            add_habit(session, user_id, text_name)
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Your new habit - {text_name} added!"
            )
    finally:
        session.close()

async def list_habits_command(update, context):
    session = SessionLocal()
    try:
        telegram_id = update.effective_user.id
        habits= get_habits(session, telegram_id)
        texto = ""
        for habit in habits:
            texto += f"{habit.id} - {habit.name}\n"
        texto = texto.strip()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Your habits: \n{texto}"
            )
    finally:
        session.close()

async def delete_habit_command(update, context):
    session = SessionLocal()
    try:
        if not context.args:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Please, mention id of habit."
            )
            return
        if context.args[0].isdigit():
            habit_id = int(context.args[0])
            if delete_habit(session, habit_id, update.effective_user.id):
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"Habit deleted!")
            else:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"It looks like you don't have a habit with that ID.")
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Please enter the habit IDs\nYou can find them in /list.")
    finally:
        session.close()

async def done_command(update, context):
    session = SessionLocal()
    try:
        user_id = update.effective_user.id
        if not context.args:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Invalid command, please enter /done <id>"
            )
            return 
        if context.args[0].isdigit():
            habit_id = int(context.args[0])
            if get_habit_by_id(session, habit_id, user_id):
                add_completion(session, habit_id)
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="Done!"
                )
            else:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="You don't have that habit."
                )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Please enter the habit IDs\nYou can find them in /list."
            )
    finally:
        session.close()

async def streak_command(update, context):
    session = SessionLocal()
    try:
        if not context.args:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Invalid command, please enter /streak <id>"
            )
            return 
        if context.args[0].isdigit():
            habit = get_habit_by_id(session, int(context.args[0]), update.effective_user.id)
            if habit:
                count = count_completions(session, int(context.args[0]))
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"Your streak - {count}🔥")
            else:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"It seems you don't have this habit.")
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Please enter the habit IDs, you can find them in /list")
    finally:
        session.close()