class Duck:
    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('flap, flap')


class Person:
    def quack(self):
        print('I can quack like a duck!')

    def fly(self):
        print('I can flap my arms ')


def quack_and_fly(thing):
    # LBYT (Non-Pythonic way)

    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack()):
    #         thing.quack()
    #
    #     if hasattr(thing, 'fly'):
    #         if callable(thing.fly()):
    #             thing.fly()

    
    # Pythonic-way
    try:
        thing.quack()
        thing.fly()
        thing.laugh()
    except AttributeError as e:
        print(e)

    print()


duck = Duck()
quack_and_fly(duck)

person = Person()
quack_and_fly(person)

time.sleep(1)