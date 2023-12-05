
state = "unknown"

m = []

with open("./sample.txt") as fp:
    for _line in fp.readlines():
        data = _line.strip().split(" ")
        if len(data) > 0 and data[0].isnumeric():
            data = [int(x) for x in data]

            dest = data[0]
            source = data[1]
            dist = data[2]

            # Dynamically size m
            if source + dist > len(m):
                if source > len(m):
                    m += [i for i in range(source)]

                for i in range(dist):
                    if source + i > len(m):
                        m += [source + i]

            if dest + dist > len(m):
                if source > len(m):
                    m += [i for i in range(source)]

                for i in range(dist):
                    if dest + i > len(m):
                        m += [dest + i]
            
            print(source, dest, dist)
            print(m)
            m[source:source+dist] = m[dest:dest+dist]

print(min(m))

