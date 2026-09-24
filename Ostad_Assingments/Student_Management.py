class Student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.department = department
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def calculate_result(self, *marks):
        if not marks:
            return 0.0
        return sum(marks) / len(marks)

    def get_student_type(self):
        return "General Student"

    def display_info(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Dept: {self.department}, Email: {self.__email}")


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print(f"Semester: {self.semester}, Type: {self.get_student_type()}")


class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}, Type: {self.get_student_type()}")


if __name__ == "__main__":
    ug = UndergraduateStudent("Rahim", "UG-101", "rahim@mail.com", 21, "CSE", "5th")
    grad = GraduateStudent("Karim", "GR-201", "karim@mail.com", 25, "EEE", "Machine Learning")

    students = [ug, grad]
    for s in students:
        s.display_info()
        print(f"Average Result: {s.calculate_result(80, 85, 90)}")
        print("-" * 30)