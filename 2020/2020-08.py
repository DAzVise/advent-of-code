with open("inputs/2020-08.txt") as f:
    inputs = [i.strip().split(" ") for i in f.readlines()]

def follow_instructions(instructions, finished, index):
    accumulator = 0
    for instruction in instructions[index:]:
        if index in finished:
            break

        finished.append(index)

        if instruction[0] == "acc":
            num = int(instruction[1])
            accumulator += num
        elif instruction[0] == "jmp":
            num = int(instruction[1])
            index += num
            acc = follow_instructions(instructions, finished, index)
            accumulator += acc
            break
        else:
            pass
            
        index += 1

    return accumulator

def part_one(inputs):
    return follow_instructions(inputs, [], 0)

print(part_one(inputs))

def attempt_instructions(instructions, finished, index):
    accumulator = 0
    repaired = True
    for instruction in instructions[index:]:
        if index in finished:
            repaired = False
            break

        finished.append(index)

        if instruction[0] == "acc":
            num = int(instruction[1])
            accumulator += num
        elif instruction[0] == "jmp":
            num = int(instruction[1])
            index += num
            acc, repaired = attempt_instructions(instructions, finished, index)
            if not repaired:
                break
            accumulator += acc
            break
        else:
            pass
            
        index += 1

    return accumulator, repaired

def part_two(inputs):
    copies = []
    for i, instruction in enumerate(inputs):
        if instruction[0] == "jmp" or instruction[0] == "nop":
            replacement = "jmp" if instruction[0] == "nop" else "nop"
            copy = inputs.copy()
            copy[i] = [replacement, instruction[1]]
            copies.append(copy)

    for c in copies:
        accumalator, repaired = attempt_instructions(c, [], 0)
        if repaired:
            return accumalator


print(part_two(inputs))
