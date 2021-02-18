class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary


employee1 = Employee("Tushar", 26, "?")
print(f'Hi,My name is {employee1.name} age is {employee1.age} and my salary is '
      f' {employee1.salary}')

