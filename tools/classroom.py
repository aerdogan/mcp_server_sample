from data.db import SessionLocal
from models import Classroom

def register_classroom_tools(mcp):
    
    @mcp.tool()
    def create_classroom(name: str, sessionId: str = None, action: str = None, chatInput: str = None, toolCallId: str = None):
        """Yeni bir sınıf oluşturur."""
        db = SessionLocal()
        classroom = Classroom(name=name)
        db.add(classroom)
        db.commit()
        db.refresh(classroom)
        db.close()
        return {"id": classroom.id, "name": classroom.name}

    @mcp.tool()
    def list_classrooms(sessionId: str = None, action: str = None, chatInput: str = None, toolCallId: str = None):
        """Tüm sınıfları listeler."""
        db = SessionLocal()
        classrooms = db.query(Classroom).all()
        result = [{"id": c.id, "name": c.name} for c in classrooms]
        db.close()
        return result

    @mcp.tool()
    def get_classroom_id_by_name(name: str, sessionId: str = None, action: str = None, chatInput: str = None, toolCallId: str = None):
        """Adı verilen sınıfın ID değerini verir."""
        db = SessionLocal()
        classroom = db.query(Classroom).filter(name == name).first()
        db.close()
        return classroom.id