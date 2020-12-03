with open("inputs/2020-01.txt") as f:
    inputs = list(map(int, f.readlines()))

def part_one(numbers):
    for n in numbers:
        numbers_copy = numbers.copy()
        numbers_copy.remove(n)
        for num in numbers_copy:
            if n + num == 2020:
                return n * num

print(part_one(inputs))

def part_two(numbers):
    for x in numbers:
        numbers_copy = numbers.copy()
        numbers_copy.remove(x)
        for y in numbers_copy:
            numbers_copy2 = numbers.copy()
            numbers_copy2.remove(x)
            numbers_copy2.remove(y)
            for z in numbers_copy2:
                if x + y + z == 2020:
                    return x * y * z

print(part_two(inputs))
