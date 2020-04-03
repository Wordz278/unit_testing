from animal import Animal


class Dog(Animal):
    def __init__(self, food, sound):
        super().__init__(food, sound)

    def eat(self):
        return self.food

    def sounds(self):
        return self.sound


if __name__ == "__main__":
    print("==========Dog==============")
    dog = Dog("Food", "Bark")
    print(dog.eat())
    print(dog.sounds())
