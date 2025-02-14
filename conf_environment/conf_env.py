import os


class Config:
    # Database Configuration
    DATABASE_NAME = os.getenv("DATABASE_NAME", "rag_db")
    DB_USERNAME = os.getenv("DB_USERNAME", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "pinaki")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

    # LLM Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_key")
    HUGGINGFACE_MODEL = os.getenv("HUGGINGFACE_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

    # Performance Settings
    ASYNC_PROCESSING = True
