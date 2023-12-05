import re


def solve(filename):
    s = 0
    arr = [1 for _ in open(filename)]
    with open(filename, "r") as fp:
        for i, _line in enumerate(fp.readlines()):
            winners, yours = tuple(_line.strip().split(":")[1].split("|"))
            winners, yours = re.split(" +", winners.strip()), re.split(" +", yours.strip())
            winners, yours = [int(x) for x in winners], [int(x) for x in yours]
            winners, yours = set(winners), set(yours)
            
            n = len(winners & yours)
            print(n)
            if n > 0:
                for _i in range(i + 1, i + 1 + n):
                    arr[_i] += arr[i]


    print(arr)
    print(sum(arr))


solve("data.txt")
