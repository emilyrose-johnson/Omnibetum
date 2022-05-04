#
# CS 224 Spring 2022
# Programming Assignment 2
#
# This program is a word game called Omnibetum that presents 7 letters to the user
# and the user than has to make as many valid words as possible from those letters.
# This program keeps track of the letters that the user is allowed, the users
# name, score and the words that the user has come up with.
# This program will continue to run until the user enters "q" which runs
# an exit message for the user
#
# Author: Emily Johnson
# Date: March 26, 2022
#

import random

# gets name and input number from user
def main():
    print("Welcome to Omnibetum - the CS224 word game.\n\n"
          "Omnibetum is a single-player word game. You will be\n"
          "presented with seven letters from which you will form\n"
          "as many words as possible. One of the letters is\n"
          "marked with asterisks. It must appear in every word\n"
          "you enter. You may repeat letters within a word. Words\n"
          "with fewer than 4 letters will receive a score of 0.\n"
          "Scoring for others words is as follows:\n\n"
          "4 letters: 1 point\n"
          "n letters: n points (for n > 4)\n\n"
          "A word that uses all seven letters is an Omnibetum\n"
          "and scores a bonus of 7 points.\n\n"
          "Good luck!\n")

    name = input("Please enter your name: ")
    print("\nYou will now choose the game to play. Your selection\n"
          "must be the integer part of the inputs listed below.\n\n"
          "input1.txt input2.txt input3.txt input4.txt input5.txt\n"
          "input6.txt input7.txt\n\n")

    num = input("Enter the game to play: ")

    while num.isdigit() is False or not(1 <= int(num) <= 7):
        num = input("Enter a number between 1 and 7 ")

    letters, words = file(num)

    game(letters, words, name)

# reads the input file user has specified and gathers the letters and words needed
def file(num):
    f = open("./Inputs/input" + num + ".txt")

    ls = f.read()
    lines = ls.splitlines()

    letters = lines[0:7]
    words = lines[8:]

    return letters, words


# runs main game, prints menu and determines which function to call based on user input
def game(letters, words, name):
    valid = []  # list of words user has found
    score = 0

    while True:
        print(*letters[:-1], end=" "),
        print("*" + letters[6] + "*\n")
        print("Player options:\n"
              "   1: Print your score\n"
              "   2: Print your valid words\n"
              "   3: Shuffle the letters\n"
              "   h: Help\n"
              "   q: Quit game\n\n"
              "Or enter a word\n")
        inp = input("Please enter a word or menu option: ").lower()
        if inp == "q":
            menu(inp, score, valid, letters, name)
            break

        # menu call
        elif inp == "1" or inp == "2" or inp == "3" or inp == "h":
            menu(inp, score, valid, letters, name)

        # word entry
        else:
            score = check(inp, words, valid, score, letters)


# checks users word is valid or already found
# if word is new and valid word, calls good
def check(inp, words, valid, score, letters):
    if len(inp) < 4:
        print("Words need to be 4 letters long\n")
    elif not(inp in words):
        print("That word is not valid\n")
    else:
        if inp in valid:
            print("You've found this word already\n")
        else:
            score = good(inp, valid, score, letters)

    return score


# Function for when a new valid word is found, calculates score
def good(inp, valid, score, letters):
    # word is 4 letters long
    if len(inp) == 4:
        print("Good. You scored 1 point\n")
        score += 1

    else:
        omni = True

        # checks if all letters are in word
        for x in letters:
            if not(x.lower() in inp):
                omni = False
                break

        # word is omnibetum
        if omni:
            p = len(inp) + 7
            print("That’s an omnibetum! You scored " + str(p) + " points.\n")
            score += p

        # word is not omnibetum
        else:
            print("Great word! You scored " + str(len(inp)) + " points.\n")
            score += len(inp)

    valid.append(inp)
    valid.sort()
    return score


# function for when a menu option is called
def menu(inp, score, valid, letters, name):
    if inp == "1":
        print("\n" + name + ", your score is " + str(score) + "\n")
    elif inp == "2":
        print("\nYour words are:")
        for count, x in enumerate(range(len(valid))):
            if (count + 1) % 5 == 0:
                print(valid[x])
            else:
                print(valid[x], end=" ")

        print("\n")
    elif inp == "3":
        print("\nShuffling letters...\n")
        copy = letters[:-1]
        random.shuffle(copy)
        letters[:-1] = copy
    elif inp == "h":
        print()
        print("Omnibetum is a single-player word game. You will be\n"
              "presented with seven letters from which you will form\n"
              "as many words as possible. One of the letters is\n"
              "marked with asterisks. It must appear in every word\n"
              "you enter. You may repeat letters within a word. Words\n"
              "with fewer than 4 letters will receive a score of 0.\n"
              "Scoring for others words is as follows:\n\n"
              "4 letters: 1 point\n"
              "n letters: n points (for n > 4)\n\n"
              "A word that uses all seven letters is an Omnibetum\n"
              "and scores a bonus of 7 points.\n")
    elif inp == "q":
        print()
        print("You found " + str(len(valid)) + " valid words for a score of " + str(score) + ".\n\n"
              "Your words are:\n")
        print(*valid)
        print()
        print("Thank you for playing, " + name + ". Goodbye.")


if __name__ == '__main__':
    main()

