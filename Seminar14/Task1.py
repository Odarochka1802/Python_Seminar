import unittest

from Seminar13.ClassError import StudentNameError, InvalidSubjectError, InvalidTypeError, InvalidScoreError
from Seminar13.Task1 import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("John", "Doe", "Smith", "1.csv")

    def test_init_valid_names(self):
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.middle_name, "Doe")
        self.assertEqual(self.student.last_name, "Smith")

    def test_init_invalid_names(self):
        with self.assertRaises(StudentNameError):
            Student("123", "Doe", "Smith", "1.csv")
        with self.assertRaises(StudentNameError):
            Student("John", "123", "Smith", "1.csv")
        with self.assertRaises(StudentNameError):
            Student("John", "Doe", "123", "1.csv")

    def test_add_grade_valid_subject(self):
        self.student.add_grade("Math", 4)
        self.assertIn(4, self.student.subjects["Math"]["grades"])

    def test_add_grade_invalid_subject(self):
        with self.assertRaises(InvalidSubjectError):
            self.student.add_grade("History6", 3)

    def test_add_grade_invalid_type(self):
        with self.assertRaises(InvalidTypeError):
            self.student.add_grade("Math", "A")

    def test_add_grade_invalid_score(self):
        with self.assertRaises(InvalidScoreError):
            self.student.add_grade("Math", 6)

    def test_add_test_score_valid_subject(self):
        self.student.add_test_score("Physics", 85)
        self.assertIn(85, self.student.subjects["Physics"]["test_result"])

    def test_add_test_score_invalid_subject(self):
        with self.assertRaises(InvalidSubjectError):
            self.student.add_test_score("Chemistry", 90)

    def test_add_test_score_invalid_type(self):
        with self.assertRaises(InvalidTypeError):
            self.student.add_test_score("Himiya", "A")

    def test_add_test_score_invalid_score(self):
        with self.assertRaises(InvalidScoreError):
            self.student.add_test_score("Physics", -10)

    def test_average_test_score_valid_subject(self):
        self.student.add_test_score("Math", 80)
        self.student.add_test_score("Math", 90)
        average_score = self.student.average_test_score("Math")
        self.assertEqual(average_score, 85)

    def test_average_test_score_invalid_subject(self):
        with self.assertRaises(InvalidSubjectError):
            self.student.average_test_score("History6")

    def test_average_grade(self):
        self.student.add_grade("Physics", 4)
        self.student.add_grade("Math", 3)
        average_grade = self.student.average_grade()
        self.assertEqual(average_grade, 3.5)



if __name__ == '__main__':
    unittest.main()
