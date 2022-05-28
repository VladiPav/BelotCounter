gameType = "All trumps"  #can be "Clubs", "Diamonds", "Hearts", "Spades", "No trumps" or "All trumps"

detectedCards = {("Jack", "Diamonds"), 
                ("Jack", "Clubs"), 
                ("Jack", "Spades"), 
                ("Ace", "Clubs")}

total = 0

for i in detectedCards:
    if i[0] == "Jack":
        if gameType == "All trumps" or i[1] == gameType:
            total += 20
        else:
            total += 2
    elif i[0] == "Nine":
        if gameType == "All trumps" or i[1] == gameType:
            total += 14
    elif i[0] == "Ace":
        total += 11
    elif i[0] == "Ten":
        total += 10
    elif i[0] == "King":
        total += 4
    elif i[0] == "Queen":
        total += 3

print("Total:" + str(total))