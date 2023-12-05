
def parse_into_array(filename):
    ret = []
    l = 0
    with open(filename) as fp:
        for _line in fp.readlines():
            line = _line.strip()
            ret.append([c for c in line])
    return ret

def is_part(char):
    return char != '.' and not char.isnumeric()


def solve(arr):
    s = 0
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if is_part(arr[row][col]):
                for y in range(row - 1, row + 2):
                    for start_x in range(col - 1, col + 2): 
                        if y < 0 or y > len(arr):
                            continue

                        x = start_x
                        
                        # Backtrack to the earliest number char
                        found = False
                        while x >= 0 and arr[y][x].isnumeric():
                            found = True
                            x -= 1

                        if(found):
                            x += 1 # start at the last number
                            
                            # Generate numstring and overrite with "."
                            numstring = ""
                            while x < len(arr[y]) and arr[y][x].isnumeric():
                                numstring += arr[y][x]
                                arr[y][x] = "."
                                x += 1
                            
                            if(len(numstring) > 0):
                                s += int(numstring)
    print(s)


solve(parse_into_array("data.txt"))


