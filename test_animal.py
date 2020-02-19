import unittest

from animal import Animal
#from dog import Dog
#from cat import Cat
import dog
import cat

class AnimalTest(unittest.TestCase):
    def setUp(self):
        print("Unit Testing")
        self.dog = Animal("Food", "Bark")
        self.cat = Animal("Food", "Meow")


    def test_dog_eat(self):
        #Test to see that Dog eat Food not food

        print("Testing Dog Eat :")
        self.assertEqual(self.dog.food, "Food") 
    
    def test_dog_sound(self):
        #Test to see that Dog sound is Bark not Meow

        print("Testing Dog Sound :")
        self.assertEqual(self.dog.sound, "Bark")

    def test_cat_sound(self):
        #Test to see that Cat sound is Meow not Bark

        print("Testing Cat Sound :")
        self.assertEqual(self.cat.sound, "Meow")     
    
    def test_cat_eat(self):
        #Test to see that Dog eat is Food not food

        print("Testing Cat Eat :")
        self.assertEqual(self.cat.food, "Food")    
    
    if __name__ == "__main__":
        unittest.main()