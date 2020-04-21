"""
Module: comp110_lab12

Lab 12: A flash card program.
"""
import random


def get_flash_cards(filename):
    """
    Creates a dictionary of flash card questions and answers.

    Parameters:
    filename (type: string) - The name of the file containing flash card Q's/A's

    Returns:
    (type: dictionary) - A dictionary that associates questions with answers.
    """

    card_file = open(filename, 'r')

    for line in card_file:
        # Replace the following line with lines that split the line and add it to a dictionary
        # Use the `strip` function to ensure that the answer doesn't include a
        # newline character (i.e. '\n')
        pass

    return None # modify this line to return your dictionary


# To Do: Define your quiz function immediately after this line.


def main():
    pass # remove this line when implementing main


""" DO NOT MODIFY ANYTHING BELOW THIS LINE! """
if __name__ == "__main__":
    main()
