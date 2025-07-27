import re


def formatter(text):
    formatted_text = re.sub(r"python", "PYTHON", text.strip().lower())
    return formatted_text


res = formatter(input("Input text: "))


print(res)
