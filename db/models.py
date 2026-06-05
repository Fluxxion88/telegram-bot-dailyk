from sqlalchemy import Column, BigInteger, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
import dotenv

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