import re

dataSum = 0

numSpell = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"

}
with open("data.txt", "r") as f:
    for line in f:
        # print(line)
        # location = len(line)+1
        # subKey = None
        # while location >= 0:
        #     noFinds = 0
        #     location = len(line)+1
        #     for k,v in numSpell.items():
        #         tempLocation = line.find(k)
        #         if tempLocation == -1:
        #             noFinds += 1
        #         elif tempLocation < location:
        #             location = tempLocation
        #             subKey = k
        #     if noFinds > 8:
        #         break
        #     line = re.sub(subKey,numSpell[subKey],line,1)
        #     print(line)
            
        print(line)
        firstDiget = re.search(r'(\d|' + '|'.join(numSpell.keys()) + ')', line).groups()[0]
        if len(firstLen := firstDiget) != 1:
            firstDiget = numSpell[firstDiget]
        seconedDiget = re.search(r'(\d|' + '|'.join(t[::-1] for t in numSpell.keys()) + ')', line [::-1]).groups()[0]
        if len(seconedLen := seconedDiget) != 1:
            seconedDiget = numSpell[seconedDiget [::-1]]
        print(firstDiget)
        print(seconedDiget)
        num = int(firstDiget+seconedDiget)
        print(num)
        dataSum+= num
        print(dataSum)