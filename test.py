import database

from pydantic import BaseModel
from typing import Optional

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


student = Student(
    s_id=2,
    surname="Doe",
    name="John",
    email="john.doe@example.com",
    class_str="A",
    img_name="john.jpg"
)
 
# exam = Exam(
#     e_id=1,
#     t_id=1,
#     date="2021-05-01",
#     subject="Math"
# )

teacher = Teacher(
    surname="Cremers",
    name="John",
    email="test@gmx.de",
    t_id=1
)

try:
    # database.create_exam(another_student)
    database.create_teacher(teacher)
except: 
    pass

# retrieved_student = self.db.get_student_by_id(1)
# self.assertEqual(retrieved_student, student)


# print(database.read_teacher(1))