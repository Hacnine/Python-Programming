import random


class Dice:

    def ran(self):
        num1 = random.randint(1, 3)
        num2 = random.randint(1, 3)
        return num1, num2


di = Dice()
print(di.ran())