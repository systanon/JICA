comments = []
word = set()
for i in range(3):
    i = input(f"Enter product {i + 1}: ")
    comments.append(i)

for comment in comments:
    for i in comment.split():
        word.add(i)

print(word)



