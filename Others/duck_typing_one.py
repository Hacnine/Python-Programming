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
    thing.quack()
    thing.fly()

    print()

    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a Duck')


duck = Duck()
quack_and_fly(duck)

person = Person()
quack_and_fly(person)