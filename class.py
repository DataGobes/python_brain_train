# some class exercises


class Animal:

    def __init__(self, type, name, sound):

        self.type = type
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)


x = Animal(type='reptile', name='crocodile', sound='rrrr')
y = Animal('mammal', 'cow', 'booo')




