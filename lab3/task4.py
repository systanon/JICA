def reverse_words(text):
    parts = text.strip().split()
    result = [" "] * len(parts)
    for index, word in enumerate(parts):
        result[index] = word[::-1]
    return " ".join(result)


print(reverse_words(input("Enter text: ")))
