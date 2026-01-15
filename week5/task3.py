class Person:
    def __init__(self, name):
        self._name = name  # encapsulation

    def get_info(self):
        return f"Person name: {self._name}"


class Student(Person):
    def get_info(self):  # polymorphism
        return f"Student name: {self._name}"


p = Person("Alex")
s = Student("Maria")

print(p.get_info())
print(s.get_info())