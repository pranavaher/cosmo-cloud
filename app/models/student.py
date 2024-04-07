from pydantic import BaseModel, Field
from typing import Optional

class Address(BaseModel):
  city: Optional[str]
  country: Optional[str]

class StudentCreate(BaseModel):
  name: str
  age: int
  address: Address

class StudentList(BaseModel):
  name: str
  age: int

class StudentResponse(BaseModel):
  name: str
  age: int
  address: Address

class StudentUpdate(BaseModel):
  name: Optional[str]
  age: Optional[int]
  address: Address = Field(default_factory=dict)