from fastapi import APIRouter, HTTPException, Query
from app.controllers.student_controller import create_student, get_all_students
from app.models.student import StudentCreate, StudentList

router = APIRouter()

@router.post("/students", response_model=dict)
async def create_student_route(student_data: StudentCreate):
  student_id = await create_student(student_data)
  return {"id": student_id}

@router.get("/students", response_model=list[StudentList])
async def get_all_students_route(country: str = Query(None), age: int = Query(None)):
  return await get_all_students(country, age)
