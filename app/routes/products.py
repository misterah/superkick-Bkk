from fastapi import APIRouter
from models.course import Course

router = APIRouter()

@router.get("/")
async def create_course_endpoint():
    return {"hello":"555"}