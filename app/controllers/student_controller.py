from fastapi import HTTPException

from app.models.student import StudentCreate, StudentList, StudentResponse, StudentUpdate, Address
from app.db import collection

from typing import Optional
from bson import ObjectId

async def create_student(student_data: StudentCreate):
  # Extract data from Pydantic model
  student_dict = student_data.dict()

  # Insert the student into the MongoDB collection
  result = await collection.insert_one(student_dict)

  # Retrieve the inserted student ID
  student_id = str(result.inserted_id)

  return student_id

async def get_all_students(country: Optional[str] = None, age: Optional[int] = None):
  query = {}
  if country:
    query["country"] = country
  if age:
    query["age"] = {"$gte": age}

  # Retrieve the list of students from the MongoDB collection
  cursor = collection.find(query)
  students = await cursor.to_list(length=None)
  return [StudentList(**student) for student in students]

async def get_student_by_id(student_id: ObjectId):
    student = await collection.find_one({"_id": student_id})
    if student:
      return StudentResponse(**student)
    else:
      raise HTTPException(status_code=404, detail="Student not found")

async def update_student(id: str, student_update: StudentUpdate):
  student_id = ObjectId(id)
  updated_values = {k: v for k, v in student_update.dict().items() if v is not None}
  if not updated_values:
    raise HTTPException(status_code=400, detail="No fields provided for update")
  if 'address' in updated_values:
    # Convert Address object to a dictionary before saving to MongoDB
    updated_values['address'] = student_update.address.dict()
  result = await collection.update_one({"_id": student_id}, {"$set": updated_values})
  if result.matched_count == 0:
    raise HTTPException(status_code=404, detail="Student not found")

async def delete_student(student_id: str):
  result = await collection.delete_one({"_id": ObjectId(student_id)})
  return result.deleted_count