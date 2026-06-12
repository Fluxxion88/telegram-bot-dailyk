import os
import dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
dotenv.load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(bind=engine)