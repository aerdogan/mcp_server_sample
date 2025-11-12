from data.db import SessionLocal
from models import Student, Classroom

def register_student_tools(mcp):

    @mcp.tool()
    def create_student(name: str, age: int, classroom_id: int, sessionId: str = None, action: str = None, chatInput: str = None, toolCallId: str = None):
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
    def list_students(classroom_id: int = None, sessionId: str = None, action: str = None, chatInput: str = None, toolCallId: str = None):
        """Tüm öğrencileri veya bir sınıfa ait öğrencileri listeler."""
        db = SessionLocal()
        query = db.query(Student)
        if classroom_id:
            query = query.filter(Student.classroom_id == classroom_id)
        students = query.all()
        result = [{"id": s.id, "name": s.name, "age": s.age, "classroom_id": s.classroom_id} for s in students]
        db.close()
        return result
