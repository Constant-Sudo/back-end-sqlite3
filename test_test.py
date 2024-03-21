import unittest
from database 
from models import Student

class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.db = 

    def tearDown(self):
        self.db.close()

    def test_add_student(self):
        student = Student(
            s_id=1,
            surname="Doe",
            name="John",
            email="john.doe@example.com",
            class_str="A",
            img_name="john.jpg"
        )
        self.db.add_student(student)
        retrieved_student = self.db.get_student_by_id(1)
        self.assertEqual(retrieved_student, student)

    def test_remove_student(self):
        student = Student(
            s_id=1,
            surname="Doe",
            name="John",
            email="john.doe@example.com",
            class_str="A",
            img_name="john.jpg"
        )
        self.db.add_student(student)
        self.db.remove_student(1)
        retrieved_student = self.db.get_student_by_id(1)
        self.assertIsNone(retrieved_student)

    def test_update_student(self):
        student = Student(
            s_id=1,
            surname="Doe",
            name="John",
            email="john.doe@example.com",
            class_str="A",
            img_name="john.jpg"
        )
        self.db.add_student(student)
        updated_student = Student(
            s_id=1,
            surname="Smith",
            name="Jane",
            email="jane.smith@example.com",
            class_str="B",
            img_name="jane.jpg"
        )
        self.db.update_student(updated_student)
        retrieved_student = self.db.get_student_by_id(1)
        self.assertEqual(retrieved_student, updated_student)

    def test_get_student_by_id(self):
        student = Student(
            s_id=1,
            surname="Doe",
            name="John",
            email="john.doe@example.com",
            class_str="A",
            img_name="john.jpg"
        )
        self.db.add_student(student)
        retrieved_student = self.db.get_student_by_id(1)
        self.assertEqual(retrieved_student, student)

if __name__ == '__main__':
    unittest.main()import unittest
from database import Database
from models import Student

class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def tearDown(self):
        self.db.close()

    def test_add_student(self):
        student = Student(
            s_id=1,
            surname="Doe",
            name="John",
            email="john.doe@example.com",
            class_str="A",
            img_name="john.jpg"
        )
        self.db.add_student(student)
        retrieved_student = self.db.get_student_by_id(1)
        self.assertEqual(retrieved_student, student)

    def test_remove_student(self):
        student = Student(
            s_id=1,
            surname="Doe",
            name="John",
            email="john.doe@example.com",
            class_str="A",
            img_name="john.jpg"
        )
        self.db.add_student(student)
        self.db.remove_student(1)
        retrieved_student = self.db.get_student_by_id(1)
        self.assertIsNone(retrieved_student)

    def test_update_student(self):
        student = Student(
            s_id=1,
            surname="Doe",
            name="John",
            email="john.doe@example.com",
            class_str="A",
            img_name="john.jpg"
        )
        self.db.add_student(student)
        updated_student = Student(
            s_id=1,
            surname="Smith",
            name="Jane",
            email="jane.smith@example.com",
            class_str="B",
            img_name="jane.jpg"
        )
        self.db.update_student(updated_student)
        retrieved_student = self.db.get_student_by_id(1)
        self.assertEqual(retrieved_student, updated_student)

    def test_get_student_by_id(self):
        student = Student(
            s_id=1,
            surname="Doe",
            name="John",
            email="john.doe@example.com",
            class_str="A",
            img_name="john.jpg"
        )
        self.db.add_student(student)
        retrieved_student = self.db.get_student_by_id(1)
        self.assertEqual(retrieved_student, student)

if __name__ == '__main__':
    unittest.main()