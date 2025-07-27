def reverse_words(text):
    parts = text.strip().split()
    result = []
    for word in parts:
        result.append(word[::-1])
    return " ".join(result)


print(reverse_words(input("Enter text: ")))
