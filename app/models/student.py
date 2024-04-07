from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
  city: str
  country: str

class StudentCreate(BaseModel):
  name: str
  age: int
  address: Address

class StudentList(BaseModel):
  name: str
  age: int
