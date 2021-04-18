"""Imported random function to get random numbers on line 182, 184, & 185"""
import random

__author__ = "Billy Jean Baptiste"
"""This is an introduction to a very basic and somewhat familiar concept card
game called "Kazino"""""
"""Similar like BlackJack, cards have numerical vales and can be added together
,"""
"""but the biggest difference is face cards have increasing value, J-A == 11-14
, respectively."""


# This is a introduction to obtain the user's name and age

def main():
    """The function starts the entire program"""
    # Code to use boolean value "True" as a not False
    continue_program = not False
    while continue_program:
        # Greeting function
        greeting()
        users_name = input()
        # Code to make sure user enters a valid age
        valid_age = True
        users_age = 0
        while valid_age:
            try:
                users_age = int(input("Please enter your age "))
                valid_age = False
            except ValueError:
                print("Quit messing around and enter a numerical number.")

        # This variable is to store the age minimum to play the game.
        old_enough = 13
        if old_enough > users_age or users_age > 65:
            print("Sorry, you are not old eligible to play", end=".")
            # If the user is not old enough, the program is ended
            continue_program = False
        else:
            print("Congratulations", str(
                users_name.capitalize()) + ", you're pretty old! Let's get"
                                           " started!", )

            # Here, we will introduce an interactive way to the "How to play"
            user_input = input(
                "Are you familiar with the game Black Jack?: Y or N? ")

            if user_input.lower() == "y":
                print(
                    "Great, so you should be familiar with the concept in this"
                    " game.")
            elif user_input.lower() == "n":
                print("Lets go over the basics.")
            else:
                print("Invalid selection. Lets go over the basics.")

            print(
                "In Black Jack, every number-card's value is equal to itself"
                " and every face card is 10.")
            print("But in Kazino, it's slightly different.")
            # variable for how many cards are in a deck
            number_of_cards_in_deck = 52

            user_guessed_number = int(input(
                "But first, do you know the number of cards in a deck of card?"
                " Enter a number "))

            if user_guessed_number != number_of_cards_in_deck:
                print(
                    "NOOOOOOOOOOOOO! I see we definitely need to go through"
                    " the basics. "
                    "Well, there are 52 cards in a deck")
            else:
                print("That's incorrect. Just kidding, that's correct. "
                      "Hmmmmm, maybe we don't have to go through the basic")

            # All the face cards numerical assigned values
            # Assigned multiple variables to multiple values,
            # this is to save space
            # Create variables for all the card values
            card_number2, card_number3, card_number4, card_number5 = 2, 3, 4, 5

            ace1_card = 1
            ace14_card = 14
            jack_card = 11
            queen_card = 12
            king_card = 13

            # These prompts and statements are to inform users
            # on the game concepts
            # The indented print statements are just for structure
            # These statements also introduces the restrictions in the game
            print("So, in this game, each card has a numerical value "
                  "\nand you add, subtract, multiple or divide them together, "
                  "but you have to be explicit."
                  "\nYou're only limited from 1 to 14."
                  "\nStarting from the Jack face card."
                  " A Jack has a value of 11 in this game, \nA queen is worth",
                  queen_card, " "
                              "and a king is ",
                  king_card, ".", sep="")

            input(
                "Can you make an educated guess to what an ace is equal to? ")

            print(
                "It is a good guess to say 14, \nbut just like Black Jack, "
                "an ace is valued at",
                ace1_card, "too"
                           "\nand we can add them with other numbers "
                           "in the deck like 2."
                           " So, a jack plus 2 will be",
                to_add(jack_card, card_number2),
                "\nA queen is valued at 12, plus 2, that's",
                to_add(queen_card, card_number2),
                "and a king plus 2 is",
                str(to_add(king_card, card_number2)) + ".")

            print("Subtracting is pretty is easy as long as "
                  "you get a positive integer and not zero. "
                  "\nSo a king subtracted by a queen,",
                  str(to_subtract(king_card, queen_card)) + ", ")
            print("is fine but not the other way around. "
                  "\nWhen multiplying, you're restricted to going over 14, "
                  "so multiplying a jack and a 2 gives you ",
                  multiply(jack_card, card_number2),

                  "\nAnd that's not allowed. But on the contrary,"
                  " dividing is fine as long as your numbers are divisible."
                  "\nSo dividing a queen and a 4, you get",
                  divisible_numbers(queen_card, card_number4),
                  "or", str(to_divide(queen_card, card_number4)) +
                  ".\\nDividing a king by a queen won't work "
                  "\nbecause you get a remainder of",
                  str(king_card % queen_card) + ".")
            print("\nTechnically, you can use exponential "
                  "but only between 2 and 3, like 2 to 3rd power is",
                  str(to_the_power(card_number2, card_number3)) + ".")

            user_input = input(
                "If what you learned, can you divide a queen with a 2 card? "
                "Y or N? ")
            while user_input.lower() != "y" and user_input.lower() != 'n':
                print("Invalid entry")
                user_input = input("Try again ")
            if user_input.lower() == "y":
                print("Correct!")
            else:
                print("Incorrect")

            user_guessed_number = input(
                "Now what does an ace and a 2 give us? ")

            # Continued restrictions
            print(user_guessed_number)
            print("If you guessed", to_add(ace14_card, card_number2),
                  "you're right mathematically, "
                  "\nbut wrong in Kazino, because that's ILLEGAL, "
                  "so stop breaking the rules. "
                  "\nThe correct answer is just",
                  to_add(ace1_card, card_number2),
                  "\nAdding 2 and a king doesnt work because that gives you",
                  to_add(king_card, card_number2),
                  "and like I said before, that's ILLEGAL.")
            print(
                "In the instance where you cannot do any operations, "
                "you have to drop a card and end your turn")
            print(
                "So by now, you should have a decent understanding on "
                "how to play.")

            print(
                "Lets start with a mini game with just adding and subtracting "
                "to see if you understand the concepts."
                "let, disregard any restrictions for now")

            # Mini tutorial of the game
            # condition to continue mini game
            current_number_value = 0
            # random number for the number values, expect 14, because 14 is
            # also considered as 1
            random_card_number = random.randint(1, 13)
            rounds_in_game = 1
            your_card_number = random.randint(1, 13)
            opponent_card_number = random.randint(1, 13)
            rounds = 2
            while rounds > 0:
                for games in range(rounds_in_game):
                    print("You have", random_card_number, "and",
                          your_card_number)
                    print("Your opponent plays", opponent_card_number,
                          "What is your next move?")
                    print("1 to add")
                    print("2 to subtract")
                    user_input = input()
                    for operations in range(rounds_in_game):
                        if user_input == "1":
                            print("Which card do you want to add?")
                            print("press 1 for",
                                  str(random_card_number) + ", press 2 for",
                                  your_card_number)
                            user_input = input()
                            if user_input == "1":
                                current_number_value = to_add(
                                    random_card_number, opponent_card_number)
                                print("You now have", current_number_value)
                            if user_input == "2":
                                current_number_value = to_add(your_card_number,
                                                              opponent_card_number)
                                print("You have", current_number_value)
                        if user_input == "2":
                            print("Which card do you want to subtract?")
                            print("press 1 for",
                                  str(random_card_number) + ", press 2 for",
                                  your_card_number)
                            user_input = input()
                            if user_input == "1":
                                current_number_value = to_subtract(
                                    opponent_card_number, random_card_number)
                                print("You now have", current_number_value)
                            if user_input == "2":
                                current_number_value = to_subtract(
                                    opponent_card_number, your_card_number)
                            print("You now have", current_number_value)
                        rounds -= 1
            print("Thanks for playing. Version 3.00 will be out soon!")


# defined functions for the operations in the programs

def to_add(num1, num2):
    """This function accepts two numbers and returns the sum"""
    return num1 + num2


def to_subtract(num1, num2):
    """This function accepts two numbers and returns the difference"""
    return abs(num1 - num2)


def to_divide(num1, num2):
    """This function accepts two numbers and returns the quotient"""
    return num1 / num2


def divisible_numbers(num1, num2):
    """This function accepts two numbers a"""
    return num1 // num2


def multiply(num1, num2):
    """This function finds multiplies two number together"""
    return num1 * num2


def to_the_power(num1, num2):
    """This function takes the first number and raise it to the power of the
    next number"""
    return num1 ** num2


def greeting():
    """This function is the greeting message at the beginning of the
    program"""
    print("Welcome. " * 3)
    print("This is version 2.00 to Kazino. Please enter your name")


main()
