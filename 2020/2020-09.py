with open("inputs/2020-09.txt") as f:
    inputs = inputs = list(map(int, f.readlines()))

def get_invalid_number(numbers):
    loaded = numbers[:25]
    for num in numbers[25:]:
        match = False
        for number in loaded:
            result = num - number
            if result in loaded and result != number:
                loaded.append(num)
                loaded.pop(0)
                match = True
                break

        if not match:
            return num

def part_one(inputs):
    return get_invalid_number(inputs)


print(part_one(inputs))

def part_two(inputs):
    invalid = get_invalid_number(inputs)
    index = 0
    while True:
        result = 0
        used = []
        for num in inputs[index:]:
            result += num
            used.append(num)
            if result == invalid:
                return max(used) + min(used)

            if result > invalid:
                break

        index += 1

print(part_two(inputs))
