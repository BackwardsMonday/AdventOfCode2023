import re
import sys

dataSum = 0
dataSum2 = 0
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
        curentNum2 = ""
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
            if charater == "*":
                print("* found")
                gearParts = []
                tempAray = [temp[:] for temp in textAray]
                for i in range(-1, 2):
                        for k in range(-1, 2):
                            if x+i < 0 or y+k < 0 or x+i > len(textAray)-1 or y+i > len(line)-1:
                                continue
                            testChar = tempAray[x+i][y+k]
                            if testChar.isnumeric():
                                print(f"{testChar} is numeric")
                                startY = y+k
                                if tempAray[x+i][y+k-1].isnumeric():
                                    for j in range(len(line)):
                                        if tempAray[x+i][y+k-j].isnumeric():
                                            startY = y+k-j
                                        else:
                                            break
                                for j in range(len(line)):
                                    print(f"j: {j}")
                                    testY = startY+j
                                    testChar = tempAray[x+i][testY]
                                    if testChar.isnumeric():
                                        curentNum2 += testChar
                                        tempAray[x+i][testY] = "?"
                                        print(curentNum2)
                                    else:
                                        gearParts.append(curentNum2)
                                        print(f"apended: {curentNum2}.")
                                        curentNum2 = ""
                                        break
                if len(gearParts) == 2:
                    print(f"gear parts: {gearParts}")
                    gearRatio = int(gearParts[0])*int(gearParts[1])
                    print(gearRatio)
                    dataSum2 += gearRatio


    print(dataSum)
    print(dataSum2)
        

            