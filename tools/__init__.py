from .classroom import register_classroom_tools
from .student import register_student_tools

def register_tools(mcp):
    register_classroom_tools(mcp)
    register_student_tools(mcp)
