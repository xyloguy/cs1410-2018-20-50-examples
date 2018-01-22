def read_descriptors():
    file = open('descriptors.txt', 'r')
    words = []
    line = file.readline().rstrip()
    word = ''
    for char in line:
        if char != ',':
            word += char
        else:
            word = word.strip()
            words.append(word)
            word = ''
    return words


def main():
    print(read_descriptors())


if __name__ == '__main__':
    main()
