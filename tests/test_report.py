import unittest
import sys

sys.path.insert(0, ".")

from src.report import generate_report


class TestStudentReport(unittest.TestCase):

    def setUp(self):
        self.students = [
            ("Arun", 85),
            ("Bala", 72),
            ("Kumar", 91),
            ("Ravi", 45),
            ("Priya", 88)
        ]

    def test_total_students(self):
        report = generate_report(self.students)
        self.assertIn("Total Students: 5", report)

    def test_average_marks(self):
        report = generate_report(self.students)
        self.assertIn("Average Marks: 76.20", report)

    def test_topper(self):
        report = generate_report(self.students)
        self.assertIn("Topper: Kumar", report)

    def test_passed_students(self):
        report = generate_report(self.students)
        self.assertIn("Passed Students: 4", report)

    def test_failed_students(self):
        report = generate_report(self.students)
        self.assertIn("Failed Students: 1", report)


if __name__ == "__main__":
    unittest.main()
