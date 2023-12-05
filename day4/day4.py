import re
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
with open("../day4/data.txt", "r") as f:
    cards = f.readlines()
    cardsCopy = cards.copy()
    i=0
    cardIter = iter(cardsCopy)
    while card := next(cardIter, False):
        #TODO use re to find card number
        cardNumber = int(re.search(r"^Card\D*(\d*):", card).groups()[0])
        print(cardNumber)
        card = card.split(":")[1]
        winingNums = card.split("|")[0].split()
        cardNums = card.split("|")[1].split()
        cardWins = 0
        for num in cardNums:
            if num in winingNums:
                cardWins += 1
        if cardWins > 0:
            for k in range(cardWins):
                #replace the i in "i+k+1" with card number. Keep the i in "i+1" as i
                cardsCopy.insert(i+1, cards[cardNumber+k])
        i+=1
        
    print(dataSum)
    print(len(cardsCopy))