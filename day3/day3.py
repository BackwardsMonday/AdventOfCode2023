import re

dataSum = 0
textAray = []

def isSymble(charater):
    if not charater.isnumeric() and not charater.isalpha() and charater != "." and charater != "\n":
        return True
    else:
        return False

with open("../day3/data.txt") as f:
    for i, line in enumerate(f):
        textAray.append([])
        for k, letter in enumerate(line):
            textAray[i].append(letter)
    print(len(textAray))
    for x, line in enumerate(textAray):
        curentNum = ""
        partNum = False
        for y, charater in enumerate(line):
            if charater.isnumeric():
                curentNum += charater
                if partNum:
                    continue
                else:
                    for i in range(-1, 2):
                        for k in range(-1, 2):
                            if x+i < 0 or y+k < 0 or x+i > len(textAray)-1 or y+i > len(line)-1:
                                continue
                            testChar = textAray[x+i][y+k]
                            if isSymble(testChar):
                                partNum = True
            if (not charater.isnumeric() or y == len(line)-1) and curentNum:
                if partNum:
                    dataSum += int(curentNum)
                    partNum = False
                curentNum = ""
    print(dataSum)
        

            