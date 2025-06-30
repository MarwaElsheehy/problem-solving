class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"
person_one = Person("john", 34)
print(person_one.info)
