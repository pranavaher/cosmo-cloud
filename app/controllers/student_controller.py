from app.models.student import StudentCreate
from app.db import collection  # Import the MongoDB collection object

async def create_student(student_data: StudentCreate):
  # Extract data from Pydantic model
  student_dict = student_data.dict()

  # Insert the student into the MongoDB collection
  result = await collection.insert_one(student_dict)

  # Retrieve the inserted student ID
  student_id = str(result.inserted_id)

  return student_id

