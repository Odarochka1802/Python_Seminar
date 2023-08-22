class StudentNameError(Exception):
    def __init__(self,
                 message="Имя студента введено неверно. Оно должно содержать только буквы и начинаться с заглавной буквы."):
        self.message = message
        super().__init__(self.message)


class InvalidSubjectError(Exception):
    def __init__(self, message="Предмет не найден в файле CSV."):
        self.message = message
        super().__init__(self.message)


class InvalidScoreError(Exception):
    def __init__(self, message="Оценки должны быть от 2 до 5, а результаты тестов от 0 до 100."):
        self.message = message
        super().__init__(self.message)


class InvalidTypeError(Exception):
    def __init__(self, grade,message_9=" "):
        self.grade = grade
        self.message = f"Оценка '{self.grade}' должна быть числом."
        super().__init__(self.message)
