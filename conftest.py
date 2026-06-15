import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base          

@pytest.fixture                     
def session():
    engine = create_engine("sqlite:///:memory:")   
    Base.metadata.create_all(engine)               
    TestSession = sessionmaker(bind=engine)        
    s = TestSession()                              
    yield s                                        
    s.close()                                      