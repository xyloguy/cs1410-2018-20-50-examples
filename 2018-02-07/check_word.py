class Player:
    def __init__(self, name):
        self.name = name
        self.letters = []

    def check_word(self, word):
        c = self.letters[:]
        for char in word:
            found = False
            for i in range(len(c)):
                if char == c[i]:
                    found = True
                    c.pop(i)
                    break
            if not found:
                return False
        self.letters = c
        return True

def main():
    p = Player('Luke')
    # you might consider temporarily forcing the letters while testing
    # make sure to reference your datamember storing the letters.
    p.letters = ['n', 'e', 'f', 'g', 'e', 'a', 'z']
    print(p.letters)  #-> ['n', 'e', 'f', 'g', 'e', 'a', 'z']
    print(p.check_word('feed'))  #-> False
    print(p.letters)  #-> ['n', 'e', 'f', 'g', 'e', 'a', 'z']
    print(p.check_word('gag'))  #-> False
    print(p.letters)  #-> ['n', 'e', 'f', 'g', 'e', 'a', 'z']
    print(p.check_word('gene'))  #-> True
    print(p.letters)  #-> ['f', 'a', 'z']

main()