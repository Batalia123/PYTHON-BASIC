"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

import os, sys
sys.path.append('/Users/nwykpis/PYTHON-BASIC/practice/2_python_part_2')

from task_classes import *
from datetime import datetime, timedelta
import unittest

class TestHomework(unittest.TestCase):
    def test_homework_creation(self):
        homework = Homework("Math Assignment", 5)
        self.assertEqual(homework.text, "Math Assignment")
        self.assertIsInstance(homework.deadline, datetime)
        self.assertIsInstance(homework.created, datetime)

    def test_homework_is_active(self):
        homework = Homework("Science Project", 2)
        self.assertTrue(homework.is_active())

    def test_homework_is_not_active(self):
        homework = Homework("History Essay", 1)
        homework.deadline -= timedelta(days=2)  # Set deadline to the past
        self.assertFalse(homework.is_active())


class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student("Doe", "John")
        self.assertEqual(student.last_name, "Doe")
        self.assertEqual(student.first_name, "John")

    def test_do_homework_on_time(self):
        teacher = Teacher("Smith", "Alice")
        homework = teacher.create_homework("English Assignment", 3)
        student = Student("Doe", "Jane")
        result = student.do_homework(homework)
        self.assertEqual(result, homework)


class TestTeacher(unittest.TestCase):
    def test_teacher_creation(self):
        teacher = Teacher("Smith", "Alice")
        self.assertEqual(teacher.last_name, "Smith")
        self.assertEqual(teacher.first_name, "Alice")

    def test_create_homework(self):
        teacher = Teacher("Smith", "Alice")
        homework = teacher.create_homework("Physics Assignment", 4)
        self.assertIsInstance(homework, Homework)


if __name__ == "__main__":
    unittest.main() 