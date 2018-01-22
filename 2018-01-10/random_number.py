import random


def random_number(length=2):
    n = random.randrange(1, 10 ** length)
    n = str(n)
    while len(n) < length:
        n = '0' + n
    return n


def main():
    print(random_number(10))


if __name__ == '__main__':
    main()
