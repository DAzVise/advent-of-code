with open("inputs/2020-03.txt") as f:
    inputs = [i.strip() for i in f.readlines()]

def part_one(inputs, right=3, down=1):
    current_point = (inputs[0][0], 0)
    line = 0
    maximum_size = len(inputs[0])
    trees_encountered = 0

    while line < len(inputs) - 1:
        line += down
        index = current_point[1] + right
        if index > maximum_size - 1:
            index = index - maximum_size
            
        location = inputs[line][index]
        current_point = (location, index)

        if current_point[0] == "#": # a Tree
            trees_encountered += 1

    return trees_encountered

print(part_one(inputs))

def part_two(inputs):
    results = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slopes:
        results.append(part_one(inputs, right=slope[0], down=slope[1]))

    result = 1
    for i in results:
        result = i * result

    return result

print(part_two(inputs))
