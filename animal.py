class Animal:
    def __init__(self, food, sound):
        self.food = food
        self.sound = sound

    def eat(self):
        return print(self.food)

    def sounds(self):
        return print(self.sound)

dog = Animal("Food", "Barks")
cat = Animal("Food", "Meow")

'''
print("==========Animal (Dog)==============")
dog.eat()
dog.sounds()

print("==========Animal (Cat)==============")
cat.eat()
cat.sounds()
'''