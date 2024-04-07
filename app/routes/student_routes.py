from fastapi import APIRouter, HTTPException, Query
from app.controllers.student_controller import create_student, get_all_students, get_student_by_id, update_student
from app.models.student import StudentCreate, StudentList, StudentResponse, StudentUpdate

from bson import ObjectId

router = APIRouter()

@router.post("/students", response_model=dict)
async def create_student_route(student_data: StudentCreate):
  student_id = await create_student(student_data)
  return {"id": student_id}

@router.get("/students", response_model=list[StudentList])
async def get_all_students_route(country: str = Query(None), age: int = Query(None)):
  return await get_all_students(country, age)

@router.get("/students/{student_id}", response_model=StudentResponse)
async def get_student_by_id_route(student_id: str):
  student_id = ObjectId(student_id)
  student = await get_student_by_id(student_id)
  if student:
    return student
  else:
    raise HTTPException(status_code=404, detail="Student not found")

@router.patch("/students/{id}", status_code=204)
async def update_student_route(id: str, student_update: StudentUpdate):
  print("*************")
  await update_student(id, student_update)
  return None  # Return None as there's no content in the response
