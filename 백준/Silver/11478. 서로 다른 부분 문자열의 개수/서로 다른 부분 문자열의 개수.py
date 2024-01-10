inputValue = input()
substrings = []
for i in range(len(inputValue)):
    for j in range(i + 1, len(inputValue) + 1):
        substrings.append(inputValue[i:j])

print(len((set(substrings))))