from fastapi import APIRouter, HTTPException
from app.controllers.student_controller import create_student
from app.models.student import StudentCreate

router = APIRouter()

@router.post("/students", response_model=dict)
async def create_student_route(student_data: StudentCreate):
  student_id = await create_student(student_data)
  return {"id": student_id}
