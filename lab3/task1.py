from utils.utils import prettifyDict


def lettersCount(tekst):
    list = tekst.split()
    letters = {}
    for word in list:
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters


prettifyDict(lettersCount(input("Input some text: ")))
