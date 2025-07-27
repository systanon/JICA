def student_diary(text, listKeys={"grades"}):
    parts = text.strip().split()
    result = {}

    i = 0

    while i < len(parts):
        key = parts[i]
        i += 1

        if key in listKeys:
            values = []
            while i < len(parts):
                try:
                    values.append(int(parts[i]))
                    i += 1
                except ValueError:
                    break
            result[key] = values
            result["average"] = sum(values) / len(values)
        else:
            if i < len(parts):
                result[key] = parts[i]
                i += 1
            else:
                result[key] = None


print(student_diary(input("Enter key-value: ")))
