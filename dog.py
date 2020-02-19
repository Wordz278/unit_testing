from animal import Animal

class Dog(Animal):
    def __init__(self, food, sound):
        super().__init__(food, sound)

    def eat(self):
        return print(self.food)

    def sounds(self):
        return print(self.sound)
if __name__ == "__main__":
    print("==========Dog==============")
    dog = Dog("Food", "Bark")
    dog.eat()
    dog.sounds()