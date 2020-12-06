with open("inputs/2020-06.txt") as f:
    inputs = f.read().split("\n\n")

def part_one(inputs):
    results = []
    for answers in inputs:
        answers = answers.replace("\n", "")
        answered = len(set(answers))
        results.append(answered)

    return sum(results)

print(part_one(inputs))

def part_two(inputs):
    results = []
    for answers in inputs:
        individual_answers = answers.split("\n")
        answered = set(individual_answers[0]).intersection(*individual_answers)
        results.append(len(answered))

    return sum(results)

print(part_two(inputs))