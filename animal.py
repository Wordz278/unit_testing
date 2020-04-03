class Animal:
    def __init__(self, food, sound):
        self.food = food
        self.sound = sound

    def eat(self):
        return self.food

    def sounds(self):
        return self.sound


if __name__ == "__main__":
    dog = Animal("Food", "Barks")
    cat = Animal("Food", "Meow")

    print("==========Animal (Dog)==============")
    print(dog.eat())
    print(dog.sounds())

    print("==========Animal (Cat)==============")
    print(cat.eat())
    print(cat.sounds())
