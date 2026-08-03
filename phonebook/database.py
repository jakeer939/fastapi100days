from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///./phonebook.db"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

sessionLocal = sessionmaker(
    autoflush=False,
    autocommit = False,
    bind=engine
)

# base for table models 
Base = declarative_base()