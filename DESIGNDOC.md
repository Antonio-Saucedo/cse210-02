# Hilo Game Design Documentation

---

[Hilo Specification](https://byui-cse.github.io/cse210-course-competency/abstraction/materials/hilo-specification.html)

---

## Principles used in the program
* Abstraction
  * Created the card class to be used inside the director class which is used inside of the main.py file. This allows for over 115 lines of code to be simplified into 3 lines.
  * Added the colorama library and the random library to import functions into card.py and director.py
* Version Control System (VCS)
  * Each team member used git to stage and commit changes to the program while similtaneously pulling changes to keep the program updated across all devices.
  * Github was used to house the public repository(see "Hilo Specification" link above)
---
## The Plan
The plan for this program as to have two files that fed into a main file to run the program. Each file that fed into the main file will be for a seperate class.

The first class is the Card class. To assist this class, the random library is imported. This class initialized a random integer between 1 and 13, representing cards Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King. This class also initialized the card suit between Spade, Club, Heart, and Diamond.

<<<<<<< HEAD
Card
---------------------------

| - value
| - cardsuit
---------------------------
| + getValue()
| + getCardSuit()
---------------------------

Director
---------------------------

| - play
| - guess
| - points
| - card1
| - card2
----------------------------
| + startGame()
| + getInputs()
| + results()
| + playAgain()
----------------------------
=======
The second class is the Director Class. This class imports the Card class from game.card to be used within the director class as well as importing Fore and Style from the colorama library. The Director class initializes 5 attributes which are play, guess, points, card1, and card2.

The play attribute determines if the player would like to play with a booleon variable.

The guess attribute holds an empty string.

The points attribute holds 300 points which is the starting number of points for a player in Hilo.

The card1 and the card2 attribute hold a value of 0 which gets replaced.

The start_game method holds the following code:



    def start_game(self):
        
        while self.play & (self.points > 0):
            self.card1 = Card()
            self.card2 = Card()
            print(f"\nThe card is: {self.card1.getValue()}{self.card1.cardsuit}")
            self.get_inputs()
            self.results()
            self.play_again()


This code first checks whether the play attribute is true and if the player's points are greater than 0. If that checks to be true, it will create 2 instances for each card. The user will be shown the created instance of card1 and be prompted to pick whether the instance of card2 will be higher or lower.

After the user picks whether the card will be higher or lower, the get_inputs method will be called. This method holds the following code:

    def get_inputs(self):
        if not self.play:
            return

        higher_lower = input("Higher or Lower? [h/l] ")
        while (higher_lower.lower() != "h") & (higher_lower.lower() != "l"):
            higher_lower = input("Higher or Lower? [h/l] ")
        self.guess = higher_lower

The code first checks if the play attribute is not true. If the play attribute is not true, instead of running with the rest of the method's code, it will return back to the results method.

If the play attribute is true, the code will store user input based off whether they think the instance of card2 will be higher or lower than card1. The user will type "h" or "l". There is a safety mechanism built in to repeat the prompt if the user does not input an "h" or an "l". Once the user has inputted an "h" or an "l", that answer will be stored in the guess attribute from the Director class.

After the answer is stored into the guess attribute, the get_inputs method will end and the program will return to the start_game method. Inside of the start_game method, the results method will then be called. The results method holds the following code:

    def results(self):
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

Like the get_inputs method, the results method does a check if the play attribute is true or not. If the play attribute is false, then the method will return to the start_game method. If the play attribute is true, the method will begin by printing what the card2 instance was including the suit.

Following this output, the method runs through a system that checks to see if the user's selection was correct or incorrect, thus awarding or taking away points in result of that. There is a final check to see if the user is out of points and if that is the case will print out a game over message. If the user still has points, the method will present the number of points the player has and return to the start_game method. After the results method has finished, the play_again method will be called from the start_game method. The play_again method holds the following code:

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

There is a check at the beginning of this method to determine whether the user wants to play again much like the other methods before. If the play attribute is false, the method will return to the start_game method. If the play attribute is true, the play_again method will continue.

Inside of this method, the user is prompted to play again or not. This allows them to potentially score more points. The user can input a "y" or a "n" representing yes or no. There is a check to stop a user from inputting an answer other than "y" or "n". If the answer is "n", the method prints out a game over message and sets the play attribute to False, ending the while loop inside of the start_game method. If the answer is "y", the user will loop back to the start_game method.

All of this is abstracted by the main.py file which contains the following code:


    from game.director import Director

    director = Director()
    director.start_game()

The main.py file imports the Director class from the game.director file. From there, an instance of the Director class is created and stored into the director variable. Following that storage, the start_game method is then called to run the entirety of the program.
>>>>>>> 096e24ca572d9cc49dc55fdf01b08ef0d2b76673

---
## Team Responsibilities
Shane Cook
* class and init structure on director.py
* Game Design Documentation on DESIGNDOC.md
* README.md


Antonio Saucedo

- Create project repository.
- Results method used in the Director class to display and update score.
- Debugging results and adding attributes for Director class functionality.

Godwin Iyip

- Create the Function for get_input
  - Get player input on high/low guess for the next card and update the player's total score based on input.

Manuel Cipriano

- Create the constructor of the Director Class
- Create the constructor of the Card class
- Create the functions getValue and getCardsuit for the Card class

Chinemerem Ukeje (Cole)

- Create the Funtion for play_again
  - Ask the user if they want to play again.

---
