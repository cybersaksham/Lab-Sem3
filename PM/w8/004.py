class Animal:
    @staticmethod
    def info_of_animal():
        print("I am animal")
    
    @staticmethod
    def sound_of_animal():
        print("This is my sound")

class Dog(Animal):
    @staticmethod
    def info_of_animal():
        print("I am dog")
    
    @staticmethod
    def sound_of_animal():
        print("Sound is bark")

class Cat(Animal):
    @staticmethod
    def info_of_animal():
        print("I am cat")
    
    @staticmethod
    def sound_of_animal():
        print("Sound is meow")


# Animal
animal = Animal()
animal.info_of_animal()
animal.sound_of_animal()

# Dog
dog = Dog()
dog.info_of_animal()
dog.sound_of_animal()

# Cat
cat = Cat()
cat.info_of_animal()
cat.sound_of_animal()