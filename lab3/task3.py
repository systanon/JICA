def student_diary(text, listKeys={"grades"}):
    parts = text.strip().split()
    result = {}

    i = 0

    while i < len(parts):
        if i >= len(parts):
            break

        key = parts[i]

        if key in listKeys:
            i += 1
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
            if i + 1 < len(parts):
                result[key] = parts[i + 1]
                i += 2
            else:
                result[key] = None
                i += 1
    return result


print(student_diary(input("Enter key-value: ")))
