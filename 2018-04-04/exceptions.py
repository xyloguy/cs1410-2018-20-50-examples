
class IndexMustBeAnIntegerError(ValueError):
    pass

def get_item(l):
    while True:
        index = input('give me the index of the item you want. ')
        if len(l) == 0:
            return

        try:
            index = int(index)
            return l[index]
        except ValueError:
            raise IndexMustBeAnIntegerError
        except IndexError:
            print('Invalid Index {}'.format(index))


l = [1]
print(l)
print(get_item(l))

