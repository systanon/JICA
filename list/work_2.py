word_list = input("Input words: ").split()


words_count = {}
unique = set()


for word in word_list:
    unique.add(word)
    if word == "Python":
        print("Świetnie, znasz Pythona!")
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

print(words_count)
print(unique)


