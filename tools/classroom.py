from data.db import SessionLocal
from models import Classroom

def register_classroom_tools(mcp):
    
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
