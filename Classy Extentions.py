class Animal:
    def __init__(self, name):
       self.name = name
    def speak(self):
        return f"{self.name} makes a noise."
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def speak(self):
        return super().speak()

    
animal_one = Animal("puppy")
print(animal_one.speak())
animal_two = Cat("meow", 1)
print(animal_two.speak())
