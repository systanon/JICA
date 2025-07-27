from utils.utils import prettifyDict


def lettersCount(tekst):
    letters = {}
    for letter in tekst:
        if letter and letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters


prettifyDict(lettersCount(input("Input some text: ")))
