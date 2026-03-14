class newclass:
    def __init__(self, name, result):
        self.name = name
        self.result = result
    def show(self):
        print(f"my name is {self.name}")
        print(f"my result is {self.result}")
#object create 
s2 = newclass("raju",20.23)

# methos show
s2.show()