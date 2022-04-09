class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print('I am a ' + self.name)

animal1 = Animal('gato')
animal1.talk()

animal2 = Animal('perro')
animal2.talk()