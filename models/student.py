# models/student.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data.db import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    classroom_id = Column(Integer, ForeignKey("classrooms.id"))

    classroom = relationship("Classroom", back_populates="students")
