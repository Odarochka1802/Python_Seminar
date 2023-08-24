import unittest

from Seminar10.Task1 import Cat, Dog, Cow, AnimalFactory

class AnimalTests(unittest.TestCase):

    def test_cat(self):
        cat = Cat("Garfield", "Persian", 3)

        self.assertEqual(cat.name, "Garfield")
        self.assertEqual(cat.breed, "Persian")
        self.assertEqual(cat.age, 3)
        self.assertEqual(cat.speak(), "Garfield speaks Meow!")

    def test_dog(self):
        dog = Dog("Buddy", "Golden Retriever", 5)

        self.assertEqual(dog.name, "Buddy")
        self.assertEqual(dog.breed, "Golden Retriever")
        self.assertEqual(dog.age, 5)
        self.assertEqual(dog.speak(), "Buddy speaks Woof!")

    def test_cow(self):
        cow = Cow("Daisy", "Holstein", 4)

        self.assertEqual(cow.name, "Daisy")
        self.assertEqual(cow.breed, "Holstein")
        self.assertEqual(cow.age, 4)
        self.assertEqual(cow.speak(), "Daisy speaks Mooo!")

    def test_animal_factory(self):
        factory = AnimalFactory()

        cat = factory.create_animal("cat", "Garfield", "Persian", 3)
        dog = factory.create_animal("dog", "Buddy", "Golden Retriever", 5)
        cow = factory.create_animal("cow", "Daisy", "Holstein", 4)

        self.assertIsInstance(cat, Cat)
        self.assertIsInstance(dog, Dog)
        self.assertIsInstance(cow, Cow)

if __name__ == '__main__':
    unittest.main()