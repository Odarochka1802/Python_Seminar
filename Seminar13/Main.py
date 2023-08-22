from Seminar13.Task1 import Student

valera = Student("Valera", "Petrovich", "Bosconec", "1.cvs")
print(valera.subjects)
valera.add_grade("History", "dj")
print(valera.subjects)
valera.to_cvs()
valera.average_test_score("litra")
