class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

# object create
s1 = Student("Rahim", 20)

# method call
s1.show()