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


# student = Student(
#     s_id=2,
#     surname="Doe",
#     name="John",
#     email="john.doe@example.com",
#     class_str="A",
#     img_name="john.jpg"
# )
 
graded = ExamGraded(
    e_id=1,
    s_id=2,
    criteria="Kann schnell rechnen",
    score=5
)

# teacher = Teacher(
#     surname="Cremers",
#     name="John",
#     email="test@gmx.de",
#     t_id=1
# )

try:
    # database.create_exam(another_student)
    database.create_exam_graded(graded)
    pass
except Exception as e: 
    print(str(e))

# retrieved_student = self.db.get_student_by_id(1)
# self.assertEqual(retrieved_student, student)


# print(database.read_teacher(1))
# print(database.get_all_students())
for a in database.get_all_graded_exams():
    print(a)