from db.repository import add_user, add_habit, get_habit_by_name, delete_habit, get_habits, add_completion, count_completions, get_habit_by_id
from db.models import User
import pytest
from sqlalchemy.exc import IntegrityError

def test_add_user(session):
    add_user(session, telegram_id=123, name="Leps")
    saved = session.query(User).filter(User.telegram_id == 123).first()
    assert saved is not None
    assert saved.name == "Leps"

def test_add_duplicate_user(session):
    add_user(session, telegram_id=123, name="Leps")
    with pytest.raises(IntegrityError):
        add_user(session, telegram_id=123, name="Leps")

def test_add_habit(session):
    add_user(session, telegram_id=123, name="Leps")
    add_habit(session, telegram_id=123, name="RLHF")
    habit = get_habit_by_name(session, telegram_id=123, name="RLHF")
    assert habit 

def test_delete_own_habit(session):
    add_user(session, telegram_id=123, name="Leps")
    add_habit(session, telegram_id=123, name="RLHF")
    habit_id = get_habits(session, telegram_id=123)[0].id
    delete_habit(session, habit_id, telegram_id=123)
    habit = get_habit_by_name(session, telegram_id=123, name="RLHF")
    assert not habit

def test_delete_foreign_habit(session):
    add_user(session, telegram_id=1, name="Leps")
    add_user(session, telegram_id=2, name="Leapold")
    add_habit(session, telegram_id=1, name="RLHF")
    habit_id = get_habits(session, telegram_id=1)[0].id
    delete_habit(session, habit_id, telegram_id=2)
    habit = get_habit_by_name(session, telegram_id=1, name="RLHF")
    assert habit

def test_count_completions(session):
    add_user(session, telegram_id=1, name="Leps")
    add_habit(session, telegram_id=1, name="RLHF")
    habit_id = get_habits(session, telegram_id=1)[0].id
    for i in range(3):
        add_completion(session, habit_id)
    count = count_completions(session, habit_id)
    assert count == 3

def test_get_foreign_habit_returns_none(session):
    add_user(session, telegram_id=1, name="Leps")
    add_user(session, telegram_id=2, name="Leapold")
    add_habit(session, telegram_id=1, name="RLHF")
    habit_id = get_habits(session, telegram_id=1)[0].id
    result = get_habit_by_id(session, habit_id, telegram_id=2)
    assert result is None