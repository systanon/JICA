user_comments1 = input("Enter comments: ").split()
user_comments2 = input("Enter comments: ").split()
user_comments3 = input("Enter comments: ").split()

all_comments = [*user_comments1, *user_comments2, *user_comments3]
unique_words = set(words for words in all_comments if len(words) > 5)
print(unique_words)
print(len(unique_words))

if "Python" in unique_words:
    print("Uczestnicy lubią Pythona!")