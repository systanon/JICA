test_results = (45, 67, 82, 90, 55, 74, 100, 61)

average = sum(test_results) / len(test_results)

all_above_average = [mark for mark in test_results if mark > average]

print(average)
print(all_above_average)
print(len(all_above_average))

if 100 in all_above_average:
    print("Gratulacje dla najlepszego uczestnika!")