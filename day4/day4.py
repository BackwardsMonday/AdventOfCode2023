dataSum = 0

with open("../day4/data.txt", "r") as f:
    for line in f:
        card = line.split(":")[1]
        winingNums = card.split("|")[0].split()
        cardNums = card.split("|")[1].split()
        cardPoint = 0
        for num in cardNums:
            if num in winingNums:
                if cardPoint == 0:
                    cardPoint = 1
                else:
                    cardPoint = cardPoint*2
        dataSum += cardPoint
    print(dataSum)