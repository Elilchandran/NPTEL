import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def create_connection():
    try:
        # Create the database URL using SQLAlchemy
        db_url = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        engine = create_engine(db_url)
        return engine
    except SQLAlchemyError as e:
        print(f"Error creating engine: {e}")
        return None
