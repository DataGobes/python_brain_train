# some class exercises
import numpy as np


class Animal:

    def __init__(self, order, name, sound):

        self.order = order
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)


class Array:

    def __init__(self, size):
        self.array = np.random.random_sample(size)

    def reset(self, size):
        self.array = np.random.random_sample(size)





# x = Animal(order='reptile', name='crocodile', sound='RrRr!')
# y = Animal('mammal', 'cow', 'Booo!')
