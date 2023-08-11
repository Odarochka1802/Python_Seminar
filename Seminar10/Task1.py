class Cat:
    '''A Cat with name, breed and age components.'''
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        '''Print the name of the cat.'''
        return f"The cat is called {self.name}. Its breed is {self.breed}. It age {self.age} years."

    def speak(self):
        return f"{self.name} speaks Meow!"


class Dog:
    '''A Dog with name, breed and age components.'''
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        '''Print the name of the cat.'''
        return f"The dog is called {self.name}. Its breed is {self.breed}. It age {self.age} years."

    def speak(self):
        return f"{self.name} speaks Woof!"


class Cow:
    '''A Cow with name, breed and age components.'''
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        '''Print the name of the cat.'''
        return f"The cow is called {self.name}. It\'s breed is {self.breed}. It age {self.age} years."

    def speak(self):
        return f"{self.name} speaks Mooo!"


class AnimalFactory:
    def create_animal(self, animal_type, name, breed, age):
        if animal_type.lower() == "cat":
            return Cat(name, breed, age)
        elif animal_type.lower() == "dog":
            return Dog(name, breed, age)
        elif animal_type.lower() == "cow":
            return Cow(name, breed, age)
        else:
            raise ValueError("Invalid animal type")


if __name__ == "__main__":
    factory = AnimalFactory()
    barsic = factory.create_animal("cat", "Barsic", "Persian", 3)
    bobik = factory.create_animal("dog", "Bobik", "Golden Retriever", 5)
    burenka = factory.create_animal("cow","Burenka","\'Ne znau porod korow\'", 5)

    print(barsic)
    print(bobik)
    print(burenka)

    print(barsic.speak())
    print(bobik.speak())
    print(burenka.speak())