import math

with open("inputs/2020-05.txt") as f:
    inputs = [i.strip() for i in f.readlines()]


def get_seat_id(seat):
    row = (0, 127)
    column = (0, 7)

    rows = seat[:7]
    columns = seat[7:]

    for letter in rows:
        half = sum(row) / 2
        if letter == "F":
            row = (row[0], math.floor(half))  # Lower half = round down
        else:
            row = (math.ceil(half), row[1])  # Upper half = round up

    for letter in columns:
        half = sum(column) / 2
        if letter == "L":
            column = (column[0], math.floor(half))
        else:
            column = (math.ceil(half), column[1])

    row = row[0]
    column = column[0]

    seat_id = row * 8 + column
    return seat_id

def part_one(inputs):
    seat_ids = []
    for seat in inputs:
        seat_id = get_seat_id(seat)
        seat_ids.append(seat_id)

    return max(seat_ids)

print(part_one(inputs))

def part_two(inputs):
    seat_ids = []
    for seat in inputs:
        seat_id = get_seat_id(seat)
        seat_ids.append(seat_id)
    
    for seat_id in seat_ids:
        if seat_id - 2 in seat_ids and seat_id - 1 not in seat_ids:
            return seat_id - 1

print(part_two(inputs))
