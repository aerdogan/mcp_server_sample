# server.py
from fastapi import FastAPI
from fastmcp import FastMCP
from sqlalchemy.orm import Session
from main import SessionLocal, Classroom, Student

app = FastAPI(title="School API MCP Server")

mcp = FastMCP(name="SchoolAPI-MCP", instructions="Okul yönetimi MCP sunucusu")

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- MCP TOOLS ----------
@mcp.tool()
def create_classroom(name: str):
    """Yeni bir sınıf oluşturur."""
    db = SessionLocal()
    classroom = Classroom(name=name)
    db.add(classroom)
    db.commit()
    db.refresh(classroom)
    db.close()
    return {"id": classroom.id, "name": classroom.name}


@mcp.tool()
def list_classrooms():
    """Tüm sınıfları listeler."""
    db = SessionLocal()
    classrooms = db.query(Classroom).all()
    result = [{"id": c.id, "name": c.name} for c in classrooms]
    db.close()
    return result


@mcp.tool()
def create_student(name: str, age: int, classroom_id: int):
    """Bir sınıfa öğrenci ekler."""
    db = SessionLocal()
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        db.close()
        return {"error": "Classroom not found"}
    student = Student(name=name, age=age, classroom_id=classroom_id)
    db.add(student)
    db.commit()
    db.refresh(student)
    db.close()
    return {"id": student.id, "name": student.name, "age": student.age, "classroom_id": classroom_id}


@mcp.tool()
def list_students(classroom_id: int = None):
    """Tüm öğrencileri veya bir sınıfa ait öğrencileri listeler."""
    db = SessionLocal()
    query = db.query(Student)
    if classroom_id:
        query = query.filter(Student.classroom_id == classroom_id)
    students = query.all()
    result = [{"id": s.id, "name": s.name, "age": s.age, "classroom_id": s.classroom_id} for s in students]
    db.close()
    return result


# ---------- RUN ----------
if __name__ == "__main__":
    # MCP + FastAPI birlikte çalışsın
    mcp.run(transport="http", host="localhost", port=8000)
