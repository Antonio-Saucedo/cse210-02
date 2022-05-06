from game.card import Card
from colorama import Fore
from colorama import Style
from colorama import init
init(autoreset=True)

class Director:
    # constructor function
    # this function initializes the attributes
    # attributes: 
    # points: integer - holds the score of the game
    # play_again - boolean - tracks if user wants to play again or not
    # card1: an instance of the class card - holds the card
    # card2: another instance of the class card - holds another card
    def __init__(self):
        self.play_again = True
        self.points = 300
        self.card1 = Card()
        self.card2 = Card()
        


    # manuel
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.play_again & (self.points > 0):
            print(self.card1.getValue())
            print(self.card2.getValue())
            self.results()

    # Godwin 
        """Get player input on high/low guess for the next card and update the player's total score based on input.

        Args:
            self (Director): An instance of Director.
        """

    # Antonio
    def results(self):
        """Displays the second card and the players score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.play_again:
            return

        print(Fore.BLUE + Style.BRIGHT +f"The next card was: {self.card2.getValue()}")
        print(Fore.GREEN + Style.BRIGHT + f"Your score is: {self.points}\n")

    # Cole
        """Ask the user if they want to play again. 

        Args:
            self (Director): An instance of Director.
        """
    

    