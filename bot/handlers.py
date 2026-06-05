import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
import dotenv


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