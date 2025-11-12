# models/classroom.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from data.db import Base

class Classroom(Base):
    __tablename__ = "classrooms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    students = relationship("Student", back_populates="classroom", cascade="all, delete-orphan")
