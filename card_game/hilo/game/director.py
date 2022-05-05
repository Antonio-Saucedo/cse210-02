from game.card import Card

class Director:
    # constructor function
    # this function initializes the attributes
    # attributes: 
    # points: integer - holds the score of the game
    # card1: an instance of the class card - holds the card
    # card2: another instance of the class card - holds another card
    def __init__(self):
        self.points = 300
        self.card1 = Card()
        self.card2 = Card()
        


    # start game method
    # manuel
    """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
    def start_game(self):
        print(self.card1.getValue())
        print(self.card2.getValue())

    # get inputs method 
    # Godwin 
    """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """

    # do updates function
    # Antonio
    """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
    # do outputs function
    # Cole
    """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
    

    