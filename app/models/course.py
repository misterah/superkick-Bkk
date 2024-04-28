from pydantic import BaseModel
from typing import Optional

class Course(BaseModel):
    course_code: str
    course_name: str
    description: str
