import csv


class Descriptor:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise ValueError("Имя должно начинаться с заглавной буквы и содержать только буквы.")
        setattr(instance, self._name, value)


class Student:
    first_name = Descriptor()
    middle_name = Descriptor()
    last_name = Descriptor()

    def __init__(self, first_name, middle_name, last_name, csv_path):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            self.subjects = {row[0]: {"grades": [], "test_result": []} for row in reader}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден.")
        if grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть в диапазоне от  2 до 5.")
        self.subjects[subject]["grades"].append(grade)

    def add_test_score(self, subject, score):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден.")
        if score < 0 or score > 100:
            raise ValueError("Результат теста должен быть больше 0 и не более 100 балов.")
        self.subjects[subject]["test_result"].append(score)

    def average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден.")
        scores = self.subjects[subject]["test_result"]
        return sum(scores) / len(scores) if scores else 0

    def average_grade(self):
        total_grades = [grade for subj in self.subjects.values() for grade in subj["grades"]]
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def to_cvs(self):
        with open("results.csv", "w") as csv_file:
            writer = csv.writer(csv_file)
            for subject,score in self.subjects.items():
                writer.writerow(f"{subject}: оценки {score['grades']}, результаты тестов {score['test_result']}")

if __name__ == "__main__":
    valera = Student("Valera", "Petrovich", "Bosconec", "1.cvs")
    print(valera.subjects)
    valera.add_grade("History", 5)
    print(valera.subjects)
    valera.to_cvs()
