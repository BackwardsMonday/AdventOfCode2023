import re

colorRe = {
    "red": r"(\d*) red",
    "blue": r"(\d*) blue",
    "green": r"(\d*) green"
}
dataSum = 0
with open("../day2/data.txt", "r") as f:
    for line in f:
        gameId = int(re.search(r"^\D*(\d*)\D", line).groups()[0])
        print(gameId)
        hands = line.split(":")[1].split(";")
        minRed = 0
        minBlue = 0
        minGreen = 0
        for hand in hands:
            red = re.search(colorRe["red"], hand)
            if not red:
                red = 0
            else:
                red = int(red.groups()[0])
            blue = re.search(colorRe["blue"], hand)
            if not blue:
                blue = 0
            else:
                blue = int(blue.groups()[0])
            green = re.search(colorRe["green"], hand)
            if not green:
                green = 0
            else:
                green = int(green.groups()[0])
            minRed = max(minRed, red)
            minBlue = max(minBlue, blue)
            minGreen = max(minGreen, green)
            # if red > 12 or blue > 14 or green > 13:
            #     print(f"breaking: red:{red}, blue:{blue}, green: {green}")
            #     break
        #else:
        minPower = minRed*minBlue*minGreen
        dataSum += minPower


        
    print(dataSum)