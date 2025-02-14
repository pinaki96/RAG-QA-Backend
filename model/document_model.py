import datetime
import numpy as np
from database.db_conn import Base, engine
from sqlalchemy import Column, Integer, Text, DateTime, LargeBinary
from database.db_session import session
from sklearn.metrics.pairwise import cosine_similarity
from utils.embedding_utils import generate_embedding


class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    embedding = Column(LargeBinary, nullable=True)  # Store vector embeddings
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.embedding = generate_embedding(content)  # Auto-generate embedding

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "content": self.content,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M:%S')

        }

    def save(self):
        try:
            session.add(self)
            session.commit()
            session.refresh(self)
            return self
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def get_all():
        try:
            return session.query(Document).all()
        finally:
            session.close()

    @staticmethod
    def get_by_id(doc_id):
        try:
            return session.query(Document).filter_by(id=doc_id).first()
        finally:
            session.close()

    @staticmethod
    def delete_by_id(doc_id):
        try:
            document = session.query(Document).filter_by(id=doc_id).first()
            if document:
                session.delete(document)
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def update_by_id(doc_id, name, content):
        try:
            document = session.query(Document).filter_by(id=doc_id).first()
            if document:
                document.name = name
                document.content = content
                document.embedding = generate_embedding(content)  # Regenerate embedding on update
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


Base.metadata.create_all(engine)
