import csv

from Seminar13.ClassError import StudentNameError, InvalidSubjectError, InvalidScoreError, InvalidTypeError


class Student:

    def __init__(self, first_name, middle_name, last_name, csv_path):
        if not first_name.istitle() or not first_name.isalpha() or not middle_name.istitle() or not middle_name.isalpha() or not last_name.istitle() or not last_name.isalpha():
            raise StudentNameError
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            self.subjects = {row[0]: {"grades": [], "test_result": []} for row in reader}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise InvalidSubjectError
        if type(grade) != int:
            raise InvalidTypeError(grade)
        if grade < 2 or grade > 5:
            raise InvalidScoreError
        self.subjects[subject]["grades"].append(grade)

    def add_test_score(self, subject, score):
        if subject not in self.subjects:
            raise InvalidSubjectError
        if type(score) != int:
            raise InvalidTypeError(score)
        if score < 0 or score > 100:
            raise InvalidScoreError
        self.subjects[subject]["test_result"].append(score)

    def average_test_score(self, subject):
        if subject not in self.subjects:
            raise InvalidSubjectError
        scores = self.subjects[subject]["test_result"]
        return sum(scores) / len(scores) if scores else 0

    def average_grade(self):
        total_grades = [grade for subj in self.subjects.values() for grade in subj["grades"]]
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def to_cvs(self):
        with open("results.csv", "w") as csv_file:
            writer = csv.writer(csv_file)
            for subject, score in self.subjects.items():
                writer.writerow(f"{subject}: оценки {score['grades']}, результаты тестов {score['test_result']}")
