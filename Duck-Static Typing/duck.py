class Duck:
    def walk(self):
        print('Duck is walking.')


class Horse:
    def walk(self):
        print('Horse is walking.')


class Cat:
    def talk(self):
        print('Horse is walking.')


def func(obj):
    if hasattr(obj, 'walk'):
        obj.walk()
    else:
        print(hasattr(obj, 'walk'))


cat = Cat()
func(cat)

# duck = Duck()
# func(duck)