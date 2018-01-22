import random


def random_choice(choices):
    index = random.randrange(0, len(choices))
    return choices[index]


def main():
    animals = ['dog', 'cat', 'bird', 'fish', 'rabbit']
    print(random_choice(animals))


if __name__ == '__main__':
    main()
