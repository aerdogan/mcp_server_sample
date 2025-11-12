from pydantic import BaseModel
from typing import Optional

class Model(BaseModel):
    sessionId: Optional[str] = None
    action: Optional[str] = None
    chatInput: Optional[str] = None
    toolCallId: Optional[str] = None

class ClassroomModel(Model):
    name: str

class StudentModel(Model):
    name: str
    age: int
    classroom_id: int

class StudentListModel(Model):
    classroom_id: int
