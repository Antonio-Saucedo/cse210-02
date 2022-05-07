import random
class Card:
# make the constructor of the card class
    # attributes:
    # value: integer - it holds its value (1-13)
    # cardsuit: string - it holds the cardsuit
    def __init__(self):
        self.value =  random.randint(1,13)
        cardsuits = ["♤","♡","♢","♧"]
        self.cardsuit = cardsuits[random.randint(0,3)]

    def getValue(self):
        #self.value = random.randint(1,13)
        return self.value

    def getCardSuit(self):
        return self.cardsuit