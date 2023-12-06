import re

with open("data.txt", "r") as f:
    fullText = f.read()

maps = fullText.split(":")
del maps[0]
seeds = maps.pop(0).split()
print(seeds)
for map in maps:
    lines = map.split("\n")
    for i, seed in enumerate(seeds):
        if not seed.isnumeric():
            del seeds[i]
            continue
        seed = int(seed)
        for line in lines:
            if not line:
                continue
            if line[0].isalpha():
                continue
            rangeThings = line.split()
            destiStart = int(rangeThings[0])
            sourceStart = int(rangeThings[1])
            rangeLength = int(rangeThings[2])
            if seed in range(sourceStart,sourceStart+rangeLength):
                rangeIndex = seed - sourceStart
                seeds[i] = str(range(destiStart,destiStart+rangeLength)[rangeIndex])
                print(f"{seed}Converted to {seeds[i]} in range {sourceStart}")
seeds = [int(seed) for seed in seeds]
print(min(seeds))
print(seeds)

