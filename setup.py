import sqlite3 

con = sqlite3.connect("database.db")
cur = con.cursor()

# cur.execute("CREATE TABLE exams (student_id INTEGER PRIMARY KEY, date TEXT, subject TEXT, teacher TEXT, exam_id INTEGER)")   
cur.execute("CREATE TABLE teacher (t_id INTEGER PRIMARY KEY, surname TEXT, name TEXT, email TEXT)")   
cur.execute("CREATE TABLE student (s_id INTEGER PRIMARY KEY, surname TEXT, name TEXT, email TEXT, class_str TEXT, img_name)")   
cur.execute("CREATE TABLE exam (e_id INTEGER PRIMARY KEY, t_id INTEGER, date TEXT, subject TEXT)")   
cur.execute("CREATE TABLE exam_criteria (e_id INTEGER, criteria TEXT, ability TEXT)")   
cur.execute("CREATE TABLE exam_graded (e_id INTEGER, s_id INTEGER, criteria TEXT, score INTEGER)")   
cur.execute("CREATE TABLE teacher_student (t_id INTEGER, s_id INTEGER, class_str TEXT)")   


# student_id, name, surname, class, teacher, email
# student_id, date, subject, teacher, exam_id

# cur.execute("DROP TABLE exams")


# cur.execute("""
#     INSERT INTO exams VALUES
#     (1, '2021-05-01', 'Math', 'Cremers', 1001), 
#     (2, '2021-05-01', 'Math', 'Cremers', 1002)
#     """)

# con.commit()


# res = cur.execute("SELECT * FROM exams")
# print(res.fetchall())