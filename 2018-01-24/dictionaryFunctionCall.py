def rfunction(index):
    print('this is the r function')

def lfunction(index):
    print('this was l')

def ffunction(index):
    print('this was f')

def qfunction(index):
    print('this was q')

def call_function_with_choice(index, choice):
    d = {
        'r': rfunction,
        'l': lfunction,
        'f': ffunction,
        'q': qfunction,
    }

    if choice in d:
        function = d[choice]
        function(index)
    else:
        print('invalid choice')


def main():
    index = {}
    while True:
        choice = input('what is your choice [r,l,f,q]: ')
        call_function_with_choice(index, choice)

if __name__ == '__main__':
    main()
