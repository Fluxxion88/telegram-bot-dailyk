import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base          #? твой Base из models.py

@pytest.fixture                      #? этот декоратор помечает функцию как фикстуру
def session():
    engine = create_engine("sqlite:///:memory:")   # 1. труба к базе-в-памяти
    Base.metadata.create_all(engine)               # 2. создаём таблицы по твоим моделям
    TestSession = sessionmaker(bind=engine)        # 3. фабрика сессий к этой базе
    s = TestSession()                              # 4. штампуем одну сессию
    yield s                                        # 5. отдаём её тесту
    s.close()                                      # 6. после теста — закрываем