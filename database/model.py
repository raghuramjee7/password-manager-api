from .connect import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    public_key = Column(String, nullable=False)
    created_at = Column(String, nullable=False, server_default=text("NOW()"))

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    site = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(String, nullable=False, server_default=text("NOW()"))
