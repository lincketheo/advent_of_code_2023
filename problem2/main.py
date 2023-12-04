
def parse_line_part_1(line, maxes = {"red" : 12, "blue" : 14, "green" : 13}, verbose = False):
    hands = line.split(":")[1].split(";")
    gameno = int(line.split(":")[0].split(" ")[1])

    for hand in hands:
        color_entries = hand.split(",")
        for color_entry in color_entries:
            cep = color_entry.split(" ")
            num = int(cep[1])
            color = cep[2]
            if maxes[color] < num:
                if(verbose):
                    print("Failed: ", line, color, num, maxes[color])
                return 0
    #print("Success: ", line)
    return gameno

def parse_line_part_2(line, verbose = False):
    hands = line.split(":")[1].split(";")
    gameno = int(line.split(":")[0].split(" ")[1])

    maxes = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }

    for hand in hands:
        color_entries = hand.split(",")
        for color_entry in color_entries:
            cep = color_entry.split(" ")
            num = int(cep[1])
            color = cep[2]
            if maxes[color] < num:
                maxes[color] = num
    ret = maxes["red"] * maxes["green"] * maxes["blue"]
    if(verbose):
        print(line, "\n", gameno, maxes, ret)
    return ret

    
def part_one(filename, verbose = False):
    s = 0
    with open(filename, "r") as fp:
        for line in fp.readlines():
            s += parse_line_part_1(line.strip(), verbose = verbose)
    print(s) 

def part_two(filename, verbose = False):
    s = 0
    with open(filename, "r") as fp:
        for line in fp.readlines():
            s += parse_line_part_2(line.strip(), verbose = verbose)
    print(s) 


print("Problem 2:")
print("Part 1:")
print("Sample:")
part_one("sample.txt", verbose = True)
print("Real:")
part_one("code.txt")
print("Part 2:")
print("Sample:")
part_two("sample.txt", verbose = True)
print("Real:")
part_two("code.txt")
