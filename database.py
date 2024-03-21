import sqlite3 
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


def get_all_graded_exams() -> list:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM exam_graded')
        results = cursor.fetchall()
        graded_exams = []
        for result in results:
            graded_exams.append(result)
        return graded_exams


def get_all_exams() -> list:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM exam')
        results = cursor.fetchall()
        exams = []
        for result in results:
            exam = Exam(e_id=result[0], t_id=result[1], date=result[2], subject=result[3])
            exams.append(exam)
        return exams

def get_exam_graded_by_student_id(student_id: int) -> list:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM exam_graded WHERE s_id = ?', (student_id,))
        results = cursor.fetchall()
        exam_graded_list = []
        for result in results:
            exam_graded = ExamGraded(e_id=result[0], s_id=result[1], criteria=result[2], score=result[3])
            exam_graded_list.append(exam_graded)
        return exam_graded_list


def get_graded_exams_by_subject(student_id: int, subject: str) -> list:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT exam.e_id, exam.date, exam.subject, exam_graded.criteria, exam_graded.score FROM exam JOIN exam_graded ON exam.e_id = exam_graded.e_id WHERE exam_graded.s_id = ? AND exam.subject = ?', (student_id, subject))
        results = cursor.fetchall()
        graded_exams = []
        for result in results:
            exam = Exam(e_id=result[0], t_id=None, date=result[1], subject=result[2])
            exam_graded = ExamGraded(e_id=result[0], s_id=student_id, criteria=result[3], score=result[4])
            graded_exams.append((exam, exam_graded))
        return graded_exams


def get_all_students() -> list:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM student')
        results = cursor.fetchall()
        students = []
        for result in results:
            student = Student(s_id=result[0], surname=result[1], name=result[2], email=result[3], class_str=result[4], img_name=result[5])
            students.append(student)
        return students

def get_students_in_class(class_str: str) -> list:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM student WHERE class_str = ?', (class_str,))
        results = cursor.fetchall()
        students = []
        for result in results:
            student = Student(s_id=result[0], surname=result[1], name=result[2], email=result[3], class_str=result[4], img_name=result[5])
            students.append(student)
        return students

# CRUD operations for Student
def create_student(student: Student):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO student (s_id, surname, name, email, class_str, img_name) VALUES (?, ?, ?, ?, ?, ?)',
                        (student.s_id, student.surname, student.name, student.email, student.class_str, student.img_name))
        conn.commit()

def read_student(s_id: int) -> Optional[Student]:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM student WHERE s_id = ?', (s_id,))
        result = cursor.fetchone()
        if result:
            return Student(s_id=result[0], surname=result[1], name=result[2], email=result[3], class_str=result[4], img_name=result[5])
        return None

def update_student(student: Student):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE student SET surname = ?, name = ?, email = ?, class_str = ?, img_name = ? WHERE s_id = ?',
                        (student.surname, student.name, student.email, student.class_str, student.img_name, student.s_id))
        conn.commit()

def delete_student(s_id: int):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM student WHERE s_id = ?', (s_id,))
        conn.commit()


# CRUD operations for Exam
def create_exam(exam: Exam):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO exam (e_id, t_id, date, subject) VALUES (?, ?, ?, ?)',
                        (exam.e_id, exam.t_id, exam.date, exam.subject))
        conn.commit()

def read_exam(e_id: int) -> Optional[Exam]:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM exam WHERE e_id = ?', (e_id,))
        result = cursor.fetchone()
        if result:
            return Exam(e_id=result[0], t_id=result[1], date=result[2], subject=result[3])
        return None

def update_exam(exam: Exam):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE exam SET t_id = ?, date = ?, subject = ? WHERE e_id = ?',
                        (exam.t_id, exam.date, exam.subject, exam.e_id))
        conn.commit()

def delete_exam(e_id: int):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM exam WHERE e_id = ?', (e_id,))
        conn.commit()


# CRUD operations for Teacher
def get_all_teachers() -> list:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM teacher')
        results = cursor.fetchall()
        teachers = []
        for result in results:
            teacher = Teacher(t_id=result[0], name=result[1], surname=result[2], email=result[3])
            teachers.append(teacher)
        return teachers

def create_teacher(teacher: Teacher):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO teacher (surname, name, email, t_id) VALUES (?, ?, ?, ?)',
                        (teacher.surname, teacher.name, teacher.email, teacher.t_id))
        conn.commit()

def read_teacher(t_id: int) -> Optional[Teacher]:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM teacher WHERE t_id = ?', (t_id,))
        result = cursor.fetchone()
        print(result)
        if result:
            return Teacher(t_id=result[0], name=result[1], surname=result[2], email=result[3])
        return None

def update_teacher(teacher: Teacher):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE teacher SET surname = ?, name = ?, email = ? WHERE t_id = ?',
                        (teacher.surname, teacher.name, teacher.email, teacher.t_id))
        conn.commit()

def delete_teacher(t_id: int):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM teacher WHERE t_id = ?', (t_id,))
        conn.commit()


# CRUD operations for ExamCriteria
def create_exam_criteria(exam_criteria: ExamCriteria):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO exam_criteria (e_id, criteria, ability) VALUES (?, ?, ?)',
                        (exam_criteria.e_id, exam_criteria.criteria, exam_criteria.ability))
        conn.commit()

def read_exam_criteria(e_id: int) -> Optional[ExamCriteria]:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM exam_criteria WHERE e_id = ?', (e_id,))
        result = cursor.fetchone()
        if result:
            return ExamCriteria(e_id=result[0], criteria=result[1], ability=result[2])
        return None

def update_exam_criteria(exam_criteria: ExamCriteria):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE exam_criteria SET criteria = ?, ability = ? WHERE e_id = ?',
                        (exam_criteria.criteria, exam_criteria.ability, exam_criteria.e_id))
        conn.commit()

def delete_exam_criteria(e_id: int):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM exam_criteria WHERE e_id = ?', (e_id,))
        conn.commit()


# CRUD operations for ExamGraded
def create_exam_graded(exam_graded: ExamGraded):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO exam_graded (e_id, s_id, criteria, score) VALUES (?, ?, ?, ?)',
                        (exam_graded.e_id, exam_graded.s_id, exam_graded.criteria, exam_graded.score))
        conn.commit()

def read_exam_graded(e_id: int, s_id: int) -> Optional[ExamGraded]:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM exam_graded WHERE e_id = ? AND s_id = ?', (e_id, s_id))
        result = cursor.fetchone()
        if result:
            return ExamGraded(e_id=result[0], s_id=result[1], criteria=result[2], score=result[3])
        return None

def update_exam_graded(exam_graded: ExamGraded):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE exam_graded SET criteria = ?, score = ? WHERE e_id = ? AND s_id = ?',
                        (exam_graded.criteria, exam_graded.score, exam_graded.e_id, exam_graded.s_id))
        conn.commit()

def delete_exam_graded(e_id: int, s_id: int):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM exam_graded WHERE e_id = ? AND s_id = ?', (e_id, s_id))
        conn.commit()


# CRUD operations for TeacherStudent
def create_teacher_student(teacher_student: TeacherStudent):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO teacher_student (t_id, s_id, class_str) VALUES (?, ?, ?)',
                        (teacher_student.t_id, teacher_student.s_id, teacher_student.class_str))
        conn.commit()

def read_teacher_student(t_id: int, s_id: int) -> Optional[TeacherStudent]:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM teacher_student WHERE t_id = ? AND s_id = ?', (t_id, s_id))
        result = cursor.fetchone()
        if result:
            return TeacherStudent(t_id=result[0], s_id=result[1], class_str=result[2])
        return None

def update_teacher_student(teacher_student: TeacherStudent):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE teacher_student SET class_str = ? WHERE t_id = ? AND s_id = ?',
                        (teacher_student.class_str, teacher_student.t_id, teacher_student.s_id))
        conn.commit()

def delete_teacher_student(t_id: int, s_id: int):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM teacher_student WHERE t_id = ? AND s_id = ?', (t_id, s_id))
        conn.commit()