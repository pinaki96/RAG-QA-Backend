from sqlalchemy.orm import sessionmaker, scoped_session
from database.db_conn import engine

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(SessionLocal)

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()