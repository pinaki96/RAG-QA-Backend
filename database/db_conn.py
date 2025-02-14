from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from conf_environment.conf_env import Config

# Load database Configuration from environment
database_name = Config.DATABASE_NAME
db_username = Config.DB_USERNAME
db_password = Config.DB_PASSWORD
db_host = Config.DB_HOST
db_port = Config.DB_PORT

print("PostgreSQL database")

# Create database engine
engine = create_engine(
    f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{database_name}',
    echo=False, pool_size=50, max_overflow=200, pool_pre_ping=True, pool_recycle=1800
)

# Base model
Base = declarative_base()

print("=======================POSTGRESQL CONNECTED==================================")
