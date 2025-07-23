word_list = input("Input words: ").split()


words_count = {}
unique = set()


for word in word_list:
    unique.add(word)
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

print(words_count)
print(unique)
if "Python" in unique:
    print("Świetnie, znasz Pythona!")