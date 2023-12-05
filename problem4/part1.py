import re


def solve(filename):
    s = 0
    with open(filename, "r") as fp:
        for _line in fp.readlines():
            winners, yours = tuple(_line.strip().split(":")[1].split("|"))
            winners, yours = re.split(" +", winners.strip()), re.split(" +", yours.strip())
            winners, yours = [int(x) for x in winners], [int(x) for x in yours]
            winners, yours = set(winners), set(yours)
            
            n = len(winners & yours)
            if n > 0:
                s += 2**(n - 1)
    print(s)

solve("data.txt")
