import database
from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    surname: str
    name: str
    clas: str
    teacher: str
    email: str
    student_id: int


class Exam(BaseModel):
    date: str
    subject: str
    teacher: str
    exam_id: int
    student_id: int


def main():

    student = Student(
        surname="Doe",
        name="John",
        clas="10A",
        teacher="Mr. Smith",
        email="john.doe@example.com",
        student_id=12345
    )
    database.add_student(student)
    print(database.get_students())


if __name__ == "__main__":
    main()