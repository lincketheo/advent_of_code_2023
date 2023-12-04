import functools 

print("Problem 1:")

digits = {
    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

# Get all unique lengths of words of digits
lengths = set()
for a in digits.keys():
    lengths |= {len(a)}

def get_first_number(text):
    for i in range(len(text)):
        if text[i].isdigit():
            return int(text[i])
    raise "Invalid string: " + text

def get_last_number(text):
    for i in range(len(text) - 1, -1, -1):
        if text[i].isdigit():
            return int(text[i])
    raise "Invalid string: " + text

def get_first_number_text_inclusive(text):
    for i in range(len(text)):
        if text[i].isdigit():
            return int(text[i])
        else:
            # For each unique substring lengths:
            for l in lengths:
                # Check if there is a substring that can match
                if l + i <= len(text):
                    # If there is - check if it's a number:
                    substr = text[i:i+l]
                    if substr in digits:
                        return digits[substr]

def get_last_number_text_inclusive(text):
    for i in range(len(text) - 1, -1, -1):
        if text[i].isdigit():
            return int(text[i])
        else:
            # For each unique substring lengths:
            for l in lengths:
                # Check if there is a substring that can match
                if l + i <= len(text):
                    # If there is - check if it's a number:
                    substr = text[i:i+l]
                    if substr in digits:
                        return digits[substr]

def part_one(filename):
    s = 0
    with open(filename, "r") as fp:
        for _line in fp.readlines():
            line = _line.strip()
            first = get_first_number(line) 
            last = get_last_number(line)
            s += int(str(first) + str(last))

    print(s)

def part_two(filename):
    s = 0
    with open(filename, "r") as fp:
        for _line in fp.readlines():
            line = _line.strip()
            first = get_first_number_text_inclusive(line) 
            last = get_last_number_text_inclusive(line)
            s += int(str(first) + str(last))

    print(s)

print("Part one:")
part_one("code.txt")

print("Part two:")
part_two("code.txt")
