from game.card import Card
from colorama import Fore
from colorama import Style

class Director:
    # constructor function
    # this function initializes the attributes
    # attributes: 
    # points: integer - holds the score of the game
    # guess - string - holds the player guess
    # play - boolean - tracks if player wants to play again or not
    # card1 - an instance of the class card - holds the card
    # card2 - another instance of the class card - holds another card
    def __init__(self):
        self.play = True
        self.guess = ""
        self.points = 300
        self.card1 = 0
        self.card2 = 0

    # manuel
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.play & (self.points > 0):
            self.card1 = Card()
            self.card2 = Card()
            print(f"\nThe card is: {self.card1.getValue()}{self.card1.cardsuit}")
            self.get_inputs()
            self.results()
            self.play_again()

    # Godwin 
        """Get player input on high/low guess for the next card and update the player's total score based on input.

        Args:
            self (Director): An instance of Director.
        """
    def get_inputs(self):
        if not self.play:
            return

        higher_lower = input("Higher or Lower? [h/l] ")
        while (higher_lower.lower() != "h") & (higher_lower.lower() != "l"):
            higher_lower = input("Higher or Lower? [h/l] ")
        self.guess = higher_lower

    # Antonio
    def results(self):
        """Displays the second card and the players score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.play:
            return

        print(Fore.BLUE + Style.BRIGHT + f"The next card was: {self.card2.getValue()}{self.card2.getCardSuit()}")

        if ((self.card1.getValue() < self.card2.getValue()) & (self.guess == "h")) | ((self.card1.getValue() > self.card2.getValue()) & (self.guess == "l")):
            self.points += 100
        elif (self.card1.getValue() == self.card2.getValue()):
            self.points = self.points
        else:
            self.points -= 75

        if self.points <= 0:
            self.play = False
            print(Fore.RED + Style.BRIGHT + "Game over. You are out of points.\n")
        else:
            print(Fore.GREEN + Style.BRIGHT + f"Your score is: {self.points}\n" + Style.RESET_ALL)

    # Cole
        """Ask the user if they want to play again. 

        Args:
            self (Director): An instance of Director.
        """
    def play_again(self):
        if not self.play:
            return

        answer = ""

        while (answer != "y" and answer != "n"):
            answer = input("Want to play again? [y/n] ").lower()

            if (answer != "n" and answer !="y"):
                print("Please enter a \"y\" or a \"n\".")

        if answer == "n":
            print ("\nGame over. You chose to stop playing.\n")
            self.play = False
        else:
            self.play = True