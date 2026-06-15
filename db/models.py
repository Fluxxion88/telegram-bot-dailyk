from sqlalchemy import Column, BigInteger, Text, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    telegram_id = Column(BigInteger, primary_key=True)
    name = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

class Habit(Base):
    __tablename__ = "habits"
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(BigInteger, ForeignKey("users.telegram_id"))
    name = Column(Text)
    description = Column(Text)
    times_a_day = Column(Integer)

class Completion(Base):
    __tablename__ = "completions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    habit_id = Column(BigInteger, ForeignKey("habits.id", ondelete="CASCADE"))
    completed_at = Column(DateTime, server_default=func.now())