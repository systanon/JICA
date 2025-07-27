def lettersCount(tekst):
    list = tekst.split()
    letters = {}
    for word in list:
        for letter in word:
            print(letter)
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters


res = lettersCount(input("Input some text: "))

print(res)
