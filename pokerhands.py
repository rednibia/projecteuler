def handcompare(hand1, hand2):
    return handcheck(hand1),handcheck(hand2)

def handcheck(hand):
    hashhand = [0]*13
    for card in hand:
        if card[0] == "2":
            hashhand[0]+=1
        elif card[0] == "3":
            hashhand[1]+=1
        elif card[0] == "4":
            hashhand[2]+=1
        elif card[0] == "5":
            hashhand[3]+=1
        elif card[0] == "6":
            hashhand[4]+=1
        elif card[0] == "7":
            hashhand[5]+=1
        elif card[0] == "8":
            hashhand[6]+=1
        elif card[0] == "9":
            hashhand[7]+=1
        elif card[0] == "T":
            hashhand[8]+=1
        elif card[0] == "J":
            hashhand[9]+=1
        elif card[0] == "Q":
            hashhand[10]+=1
        elif card[0] == "K":
            hashhand[11]+=1
        elif card[0] == "A":
            hashhand[12]+=1
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        if hashhand[8] == 1 and hashhand[9] == 1 and hashhand[10] == 1 and hashhand[11] == 1 and hashhand[12] == 1:
            return "ROYAL FLUSH"
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        for i in range(0, 7):
            if hashhand[i] == 1 and hashhand[i+1] == 1 and hashhand[i+2] == 1 and hashhand[i+3] == 1 and hashhand[i+4] == 1:
                return "STRAIGHT FLUSH"
        if hashhand[12] == 1 and hashhand[0] == 1 and hashhand[1] == 1 and hashhand[2] == 1 and hashhand[3] == 1:
            return "STRAIGHT FLUSH"
    for card in hashhand:
        if card == 4:
            return "4 of a kind!"
    for card in hashhand:
        if card == 3:
            for card2 in hashhand:
                if card2 == 2:
                    return "FULL HOUSE"
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return "FLUSH"
    for i in range(0, 8):
        if hashhand[i] == 1 and hashhand[i+1] == 1 and hashhand[i+2] == 1 and hashhand[i+3] == 1 and hashhand[i+4] == 1:
            return "STRAIGHT"
    if hashhand[12] == 1 and hashhand[0] == 1 and hashhand[1] == 1 and hashhand[2] == 1 and hashhand[3] == 1:
        return "STRAIGHT"
    for card in hashhand:
        if card == 3:
            return "3 of a kind!"
    pairs = 0
    for card in hashhand:
        if card == 2:
            pairs+=1
    if pairs == 2:
        return "TWO PAIR"
    elif pairs == 1:
        return "PAIR"

    return "NOTHING"


my_file = open('p054_poker.txt', "r")

games = []
for i in range(0, 1000):
    thestring = my_file.readline().split()
    hand1 = [list(thestring[0]),list(thestring[1]),list(thestring[2]),list(thestring[3]),list(thestring[4])]
    hand2 = [list(thestring[5]),list(thestring[6]),list(thestring[7]),list(thestring[8]),list(thestring[9])]
    hands = [hand1, hand2]
    games.append(hands)
my_file.close()

count = 0
for game in games:
    print handcompare(game[0], game[1])

