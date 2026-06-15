from db.repository import add_user
from db.models import User

def test_add_user(session):
    add_user(session, telegram_id=123, name="Leps")
    saved = session.query(User).filter(User.telegram_id == 123).first()
    assert saved is not None
    assert saved.name == "Leps"