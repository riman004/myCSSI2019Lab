pet = {
    "name": "Doggo",
    "animal": "dog",
    "species": "labrador",
    "age": 5
}

class Pet(object):
    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = False
        self.mood = "jumpy"
    def eat(self):
        print("%s is eating shrooms" % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("> %s may have eaten too much." % self.name)
            self.mood = "lethargic"
my_pet = Pet("Ein", 5, "dog")

my_pet.is_hungry = True
print("Is my pet hungry? %s" % my_pet.is_hungry)
my_pet.eat()
print("How about now? %s" % my_pet.is_hungry)
print("My pet is feeling %s" % my_pet.mood)
# my_pet = Pet("Appa", 100)
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
# my_pet = Pet("Ein", 5)
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
# my_pet = Pet("Crash", 150)
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
