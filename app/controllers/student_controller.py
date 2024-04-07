from app.models.student import StudentCreate, StudentList
from app.db import collection  # Import the MongoDB collection object

from typing import Optional

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
