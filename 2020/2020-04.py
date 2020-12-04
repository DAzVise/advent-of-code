with open("inputs/2020-04.txt") as f:
    inputs = list(map(lambda p: p.replace("\n", " "), filter(None, f.read().split("\n\n"))))


class Year:

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def is_valid(self, year):
        return len(year) == 4 and self.minimum <= int(year) <= self.maximum


class Height:

    def __init__(self):
        self.cm_minimum = 150
        self.cm_maximum = 193

        self.in_minimum = 59
        self.in_maximum = 76

    def is_valid(self, height):
        if len(height) < 3: # No measurement or no height
            return False

        measurement = height[-2:]
        height = int(height[:-2])

        if measurement == "cm": 
            return self.cm_minimum <= height <= self.cm_maximum
        else:
            return self.in_minimum <= height <= self.in_maximum


class Color:
    VALID_EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    VALID_LETTERS = ["a", "b", "c", "d", "e", "f"]

    def __init__(self, color_type):
        self.color_type = color_type

    def is_valid(self, color):
        if self.color_type == "eye":
            return color in self.VALID_EYE_COLORS

        if color[0] != "#":
            return False

        color = color.strip("#")
        if len(color) != 6:
            return False

        for char in color:
            valid = char.isdigit() or char in self.VALID_LETTERS
            if not valid:
                return False

        return True


class ID:
    
    def is_valid(self, id):
        return len(id) == 9 and id.isdigit()


REQUIRED_FIELDS = {"byr": Year(1920, 2002), "iyr": Year(2010, 2020), "eyr": Year(2020, 2030), "hgt": Height(), "hcl": Color("hair"), "ecl": Color("eye"), "pid": ID()}


def has_keys(passport):
    fields = [f.split(":")[0] for f in passport.split(" ")]
    required = list(REQUIRED_FIELDS.keys())
    return all(f in fields for f in required)


def part_one(inputs):
    valid = 0
    for passport in inputs:
        if has_keys(passport):
            valid += 1

    return valid

print(part_one(inputs))

def part_two(inputs):
    valid = 0
    for passport in inputs:
        if not has_keys(passport):
            continue

        fields = [f.split(":") for f in passport.split(" ")]
        for k, v in fields:
            if k == "cid":
                continue

            rule = REQUIRED_FIELDS[k]
            if not rule.is_valid(v):
                break
        else:
            valid += 1

    return valid

print(part_two(inputs))
