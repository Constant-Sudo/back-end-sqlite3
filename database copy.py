import sqlite3 
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


def add_student(student: Student):
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute(f"""
        INSERT INTO students VALUES
        ({student.student_id}, '{student.surname}', '{student.name}', '{student.clas}', '{student.teacher}', '{student.email}')""")
    con.commit()
    con.close()

def add_exam(exam: Exam):
    con = sqlite3.connect("exams.db")
    cur = con.cursor()
    cur.execute(f"""
        INSERT INTO exams VALUES
        ({exam.student_id}, '{exam.date}', '{exam.subject}', '{exam.teacher}', {exam.exam_id})""")
    con.commit()
    con.close()


def get_students():
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM students")
    return res.fetchall()


def get_exams():
    con = sqlite3.connect("exams.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM exams")
    return res.fetchall()


def update_student(student: Student):
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute(f"""
        UPDATE students
        SET name = '{student.name}', surname = '{student.surname}', class = '{student.clas}', teacher = '{student.teacher}', email = '{student.email}'
        """)


def update_exam(exam: Exam):
    con = sqlite3.connect("exams.db")
    cur = con.cursor()
    cur.execute(f"""
        UPDATE exams
        SET date = '{exam.date}', subject = '{exam.subject}', teacher = '{exam.teacher}', exam_id = {exam.exam_id}
        """)


def delete_student(student_id: int):
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute(f"""
        DELETE FROM students
        WHERE student_id = {student_id}
        """)


def delete_exam(exam_id: int):
    con = sqlite3.connect("exams.db")
    cur = con.cursor()
    cur.execute(f"""
        DELETE FROM exams
        WHERE exam_id = {exam_id}
        """)


# cur.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade TEXT)")

# cur.execute("CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT, surname TEXT, class TEXT, teacher TEXT, email TEXT)")
# student_id, name, surname, class, teacher, email


# cur.execute("""
#     INSERT INTO students VALUES
#     (1, 'Mueller', 'Tom', '2a', 'Cremers', 'mueller@gmx.de'), 
#     (2, 'Berger', 'Lisa', '4b', 'Cremers', 'berger@gmx.de')""")

# con.commit()


