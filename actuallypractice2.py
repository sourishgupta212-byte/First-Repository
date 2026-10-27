import math
dogs = []
class dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says Woof!")
    def dog_age(self):
        ln_age = math.log(self.age)
        dog_age = round((16 * ln_age) + 31, 2)
        print(f"""{self.name} age: {self.age}
{self.name} age in Dog years : {dog_age} """)
    def adopt_dog(self):
        dogs.append({"Name" : self.name, "Age" : self.age})
    def print_info(self):
        print(f"""Name: {self.name}
Age: {self.age}""")
Tommy = dog("Tommy", 3)
Tommy.bark()
Tommy.dog_age()
Tommy.adopt_dog()
Tommy.print_info()
Cotton = dog("Cotton", 7)
Cotton.bark()
Cotton.dog_age()
Cotton.adopt_dog()
for i in dogs:
    print(f"Name :{i["Name"]}")
    print(f"Age :{i["Age"]}")
