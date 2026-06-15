from db.models import User, Habit, Completion

def add_user(session, telegram_id, name):
    new_user = User(telegram_id=telegram_id, name=name)
    session.add(new_user)
    session.commit()

def add_habit(session, telegram_id, name, description=None, times_a_day=1):
    new_habit = Habit(telegram_id=telegram_id, name=name, description=description, times_a_day=times_a_day)
    session.add(new_habit)
    session.commit()

def add_completion(session, habit_id):
    new_completion = Completion(habit_id=habit_id)
    session.add(new_completion)
    session.commit()

def get_user(session, telegram_id):
    user = session.query(User).filter(User.telegram_id == telegram_id).first()
    return user

def get_habit_by_name(session, telegram_id, name):
    habit = session.query(Habit).filter(Habit.telegram_id == telegram_id, Habit.name == name).first()
    return habit

def get_habits(session, telegram_id):
    habits = session.query(Habit).filter(Habit.telegram_id == telegram_id).all()
    return habits

def delete_habit(session, habit_id, telegram_id):
    habit_to_delete = session.query(Habit).filter(Habit.id == habit_id, Habit.telegram_id == telegram_id).first()
    if habit_to_delete:
        session.delete(habit_to_delete)
        session.commit()
        return True
    return False

def get_habit_by_id(session, habit_id, telegram_id):
    habit = session.query(Habit).filter(Habit.id == habit_id, Habit.telegram_id == telegram_id).first()
    return habit

def count_completions(session, habit_id):
    count = session.query(Completion).filter(Completion.habit_id == habit_id).count()
    return count