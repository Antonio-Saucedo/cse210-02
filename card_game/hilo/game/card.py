import random
class Card:
# make the constructor of the card class
    #   attributes:\
    # value: integer - it holds its value (1-13)
    def __init__(self):
        self.value =  random.randint(1,13)


    def getValue(self):
        #self.value = random.randint(1,13)
        return self.value