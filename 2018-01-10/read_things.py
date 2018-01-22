def read_things():
    file = open('things.txt', 'r')
    lines = []
    for line in file:
        line = line.strip()
        lines.append(line)
    return lines


def main():
    print(read_things())


if __name__ == '__main__':
    main()
