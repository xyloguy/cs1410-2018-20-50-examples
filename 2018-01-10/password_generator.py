from random import choice

import random_number
import read_descriptors
from read_things import read_things as stuffyo


def password():
    descriptors = read_descriptors.read_descriptors()
    descriptor = choice(descriptors)
    things = stuffyo()
    thing = choice(things)
    number = random_number.random_number(3)
    return descriptor + thing + number


if __name__ == '__main__':
    for i in range(10):
        print(password())
