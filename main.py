# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, Session

DATABASE_URL = "sqlite:///./school.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# -----------------------
# MODELLER
# -----------------------
class Classroom(Base):
    __tablename__ = "classrooms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    students = relationship("Student", back_populates="classroom", cascade="all, delete-orphan")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    classroom_id = Column(Integer, ForeignKey("classrooms.id"))

    classroom = relationship("Classroom", back_populates="students")


# Veritabanını oluştur
Base.metadata.create_all(bind=engine)

# -----------------------
# FASTAPI APP
# -----------------------
app = FastAPI(title="School API with SQLite")

# Dependency (her istekte session oluşturup kapatmak için)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------
# CLASSROOM CRUD
# -----------------------
@app.post("/classrooms/", response_model=dict)
def create_classroom(name: str, db: Session = Depends(get_db)):
    classroom = Classroom(name=name)
    db.add(classroom)
    db.commit()
    db.refresh(classroom)
    return {"id": classroom.id, "name": classroom.name}

@app.get("/classrooms/", response_model=list)
def get_classrooms(db: Session = Depends(get_db)):
    return db.query(Classroom).all()

@app.get("/classrooms/{classroom_id}", response_model=dict)
def get_classroom(classroom_id: int, db: Session = Depends(get_db)):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return {"id": classroom.id, "name": classroom.name}

@app.put("/classrooms/{classroom_id}", response_model=dict)
def update_classroom(classroom_id: int, name: str, db: Session = Depends(get_db)):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    classroom.name = name
    db.commit()
    db.refresh(classroom)
    return {"id": classroom.id, "name": classroom.name}

@app.delete("/classrooms/{classroom_id}")
def delete_classroom(classroom_id: int, db: Session = Depends(get_db)):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    db.delete(classroom)
    db.commit()
    return {"message": "Classroom deleted successfully"}

# -----------------------
# STUDENT CRUD
# -----------------------
@app.post("/students/", response_model=dict)
def create_student(name: str, age: int, classroom_id: int, db: Session = Depends(get_db)):
    student = Student(name=name, age=age, classroom_id=classroom_id)
    db.add(student)
    db.commit()
    db.refresh(student)
    return {"id": student.id, "name": student.name, "age": student.age, "classroom_id": student.classroom_id}

@app.get("/students/", response_model=list)
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@app.get("/students/{student_id}", response_model=dict)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"id": student.id, "name": student.name, "age": student.age, "classroom_id": student.classroom_id}

@app.put("/students/{student_id}", response_model=dict)
def update_student(student_id: int, name: str, age: int, classroom_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.name = name
    student.age = age
    student.classroom_id = classroom_id
    db.commit()
    db.refresh(student)
    return {"id": student.id, "name": student.name, "age": student.age, "classroom_id": student.classroom_id}

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}

# -----------------------
# CLASSROOM + STUDENT ENDPOINTS
# -----------------------
@app.get("/classrooms/{classroom_id}/students", response_model=list)
def get_students_in_classroom(classroom_id: int, db: Session = Depends(get_db)):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return [{"id": s.id, "name": s.name, "age": s.age} for s in classroom.students]

@app.post("/classrooms/{classroom_id}/students", response_model=dict)
def add_student_to_classroom(classroom_id: int, name: str, age: int, db: Session = Depends(get_db)):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    student = Student(name=name, age=age, classroom_id=classroom_id)
    db.add(student)
    db.commit()
    db.refresh(student)
    return {"id": student.id, "name": student.name, "age": student.age, "classroom_id": classroom_id}
