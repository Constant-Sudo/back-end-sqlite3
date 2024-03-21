# main.py
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import database


app = FastAPI()

class Student(BaseModel):
    s_id: int
    surname: str
    name: str
    email: str
    class_str: str
    img_name: str

class Exam(BaseModel):
    e_id: int
    t_id: int
    date: str
    subject: str

class Teacher(BaseModel):
    surname: str
    name: str
    email: str
    t_id: int

class ExamCriteria(BaseModel):
    e_id: int
    criteria: str
    ability: str

class ExamGraded(BaseModel):
    e_id: int
    s_id: int
    criteria: str
    score: int # 1 - 7

class TeacherStudent(BaseModel):
    t_id: int
    s_id: int
    class_str: str 


@app.post("/student/")
async def create_item(student: Student):
    return student

@app.post("/exam/")
async def create_item(exam: Exam):
    return exam


# Get a list of all students
@app.get("/all_students/")
async def get_students():
    return database.get_all_students()

@app.get("/all_students_class/")
async def get_students_class():
    return database.get

# Get a list of all teachers
@app.get("/all_teachers/")
async def get_teacher():
    return database.get_all_teachers()

# Get a list of all exams
@app.get("/exams/")
async def get_exams():
    return database.get_exams()


# Testing
@app.get("/")
async def root():
    return {"message": "Hello There"}



# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# @app.get("/integer/{item_id}")
# async def read_item(item_id: int):
#     return {"integer": item_id}