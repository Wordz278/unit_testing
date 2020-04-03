from animal import Animal


class Cat(Animal):
    def __init__(self, food, sound):
        super().__init__(food, sound)

    def eat(self):
        return self.food

    def sounds(self):
        return self.sound


if __name__ == "__main__":
    print("==========Cat==============")
    cat = Cat("Food", "Meow")
    print(cat.eat())
    print(cat.sounds())
