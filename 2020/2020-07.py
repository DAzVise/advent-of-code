with open("inputs/2020-07.txt") as f:
    inputs = [i.strip() for i in f.readlines()]

def format_rules(inputs, keep_amount):
    bags = {}
    index = 0 if keep_amount else 1
    for rule in inputs:
        bag_name, contains = rule.split(" bags contain ")
        if contains == "no other bags.":
            bags[bag_name] = []
            continue

        contains = [" ".join(i.split(" ")[index:3]) for i in contains.split(", ")]
        bags[bag_name] = contains

    return bags

def get_contained_in(bags, search):
    options = bags[search]
    all_options = set(options)
    for option in options:
        _options = get_contained_in(bags, option)
        all_options.update(_options)

    return all_options

def part_one(inputs):
    bags = format_rules(inputs, keep_amount=False)

    reversed_bags = {}
    for bag in bags:
        contained_in = set()
        for b, contains in bags.items():
            if bag in contains:
                contained_in.add(b)

        reversed_bags[bag] = contained_in

    search = "shiny gold"
    return len(get_contained_in(reversed_bags, search))


print(part_one(inputs))

def get_contained_by(bags, search):
    search = search.split(" ")
    amount = int(search[0])
    search = " ".join(search[1:])

    result = amount
    options = bags[search]
    for option in options:
        _options = get_contained_by(bags, option) or 1
        result += _options * amount

    return result

def part_two(inputs):
    bags = format_rules(inputs, keep_amount=True)
    search = "1 shiny gold"
    return get_contained_by(bags, search) - 1 # Remove the 1 passed in the search

print(part_two(inputs))
