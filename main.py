"""Hangman Game - Food Edition

This is a simple implementation of the classic Hangman game in Python, using a vocabulary focused
on food-related words. The player attempts to guess a randomly chosen food item by suggesting letters
within a certain number of guesses. The game displays the current state of the word being guessed,
the letters that have been guessed, and the number of remaining lives.

Modules Required:
- random: To randomly select a word from a predefined list.
- ascii_images: A custom module containing ASCII art representations of the hangman stages.
- words: A custom module containing a list of food-related words to be used in the game.

Game Flow:
1. A random food word is selected from the word list.
2. The player is prompted to guess a letter.
3. The program checks if the guessed letter is in the chosen word:
   - If correct, it updates the display to show the correctly guessed letters.
   - If incorrect, it decreases the number of remaining lives.
4. The game continues until the player either guesses all letters correctly or runs out of lives.
5. The current state of the hangman (ASCII art) is displayed after each guess.

Usage:
- To play the game, simply run this script in a Python environment.
- Follow the prompts to guess letters until you either win or lose.

Example:
    python hangman.py

"""
import random
from ascii_images import stages
from words import word_list

CORRECT_LETTERS = []
#Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
print(chosen_word)
LIFES = 6
PLACEHOLDER= ""
length = len(chosen_word)
for position in range(length):
    PLACEHOLDER += "_"
print(PLACEHOLDER)

GAME_OVER = False
#Use a whole loop to let the user guess again
while not GAME_OVER :
#Ask the user to guess a letter and make guess lowercase
    guess = input("guess a letter:").lower()
    print(guess)
    if guess in CORRECT_LETTERS:
        print(f"You have already entered letter: {guess}")
    #check if the letter the user guessed is one of the letters in chosen_word
    DISPLAY = ""
    for letter in chosen_word:
        if letter == guess:
            DISPLAY += letter
            CORRECT_LETTERS.append(letter)
        elif letter in CORRECT_LETTERS:
            DISPLAY+= letter

        else:
            DISPLAY += "_"
    print(DISPLAY)
    # If guess is not equal to letter in chosen word decrease lifes by 1
    if guess not in chosen_word:
        LIFES -= 1
        print(f"########## Remaining Lifes: {LIFES}/6 ##########")
         #Printing ASCII figure from stages
        print(stages[LIFES])

        if LIFES == 0:
            GAME_OVER = True
            print("************************#//You Lose\\#************************")


    if "_" not in DISPLAY:
        GAME_OVER = True
        print("************************#//You Win\\#************************")
