
state = "unknown"

seed_to_soil = 

with open("./sample.txt") as fp:
    for _line in fp.readlines():
        if "seed-to-soil" in _line:
            state = "seed-to-soil"
            continue
        if "soil-to-fertilizer" in _line:
            state = "soil-to-fertilizer"
            continue
        if "fertilizer-to-water" in _line:
            state = "fertilizer-to-water"
            continue
        if "water-to-light" in _line:
            state = "water-to-light"
            continue
        if "light-to-temperature" in _line:
            state = "light-to-temperature"
            continue
        if "temperature-to-humidity" in _line:
            state = "temperature-to-humidity"
            continue
        if "humidity-to-location" in _line:
            state = "humidity-to-location"
            continue

        line = _line.strip()
        if len(line) == 0 or state == "unknown":
            continue

        if state == "seed-to-soil":
            arr = [int(x) for x in line.split(" ")]

            dest = arr[0]
            source = arr[1]
            dist = arr[2]
            
            sources = [source + i for i in range(dist)]
            dests = [dest + i for i in range(dist)]
            print(sources, dests)
            

