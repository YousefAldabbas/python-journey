import random


class Apple:
    counter = 0
    weight = 0

    def __init__(self,number):
        self.number = number

    def req(self):

        while self.number != 0:
            self.number -= 1
            temp = Apple.weight + (random.uniform(0.2, 0.5))
            if temp < 300:
                Apple.counter += 1
                Apple.weight = temp
                print(Apple.weight)
            else:
                break
        print(Apple.counter)

test = Apple(1000)
test.req()


