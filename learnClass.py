class learnpy:
    def __init__(self, name,age):
        self.name = name
        self.age= age

        pass

    def show(self):
        print(f"my name is {self.name}") 
        print(f"my age is {self.age}") 

w3= learnpy("ashik",23)

w3.show()