from db.connection import SessionLocal
from db.models import User, Habit, Completion

def add_user(telegram_id, name):
    session = SessionLocal()
    new_user = User(telegram_id=telegram_id, name=name)
    session.add(new_user)
    session.commit()
    session.close()

def add_habit(telegram_id, name, description=None, times_a_day=1):
    session = SessionLocal()
    new_habit = Habit(telegram_id=telegram_id, name=name, description=description, times_a_day=times_a_day)
    session.add(new_habit)
    session.commit()
    session.close()

def add_completion(habit_id):
    session = SessionLocal()
    new_completion = Completion(habit_id=habit_id)
    session.add(new_completion)
    session.commit()
    session.close()

def get_user(telegram_id):
    session = SessionLocal()
    user = session.query(User).filter(User.telegram_id == telegram_id).first()
    session.close()
    return user

def get_habit_by_name(telegram_id, name):
    session = SessionLocal()
    habit = session.query(Habit).filter(Habit.telegram_id == telegram_id, Habit.name == name).first()
    session.close()
    return habit

def get_habits(telegram_id):
    session = SessionLocal()
    habits = session.query(Habit).filter(Habit.telegram_id == telegram_id).all()
    session.close()
    return habits

def delete_habit(habit_id, telegram_id):
    session = SessionLocal()
    habit_to_delete = session.query(Habit).filter(Habit.id == habit_id, Habit.telegram_id == telegram_id).first()
    if habit_to_delete:
        session.delete(habit_to_delete)
        session.commit()
        session.close()
        return True
    session.close()
    return False

def get_habit_by_id(habit_id, telegram_id):
    session = SessionLocal()
    habit = session.query(Habit).filter(Habit.id == habit_id, Habit.telegram_id == telegram_id).first()
    session.close()
    return habit

def count_completions(habit_id):
    session = SessionLocal()
    count = session.query(Completion).filter(Completion.habit_id == habit_id).count()
    session.close()
    return count