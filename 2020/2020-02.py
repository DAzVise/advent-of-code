with open("inputs/2020-02.txt") as f:
    inputs = [i.strip().split(" ") for i in f.readlines()]

def part_one(inputs):
    valid = 0
    for i in inputs:
        _min, _max = i[0].split("-")
        char = i[1][0]
        if int(_min) <= i[2].count(char) and i[2].count(char) <= int(_max):
            valid += 1

    return valid

print(part_one(inputs))

def part_two(inputs):
    valid = 0
    for i in inputs:
        x, y = i[0].split("-")
        char = i[1][0]
        statements = [i[2][int(x) - 1] == char, i[2][int(y) - 1] == char]
        if False in statements and True in statements:
            valid += 1

    return valid

print(part_two(inputs))
