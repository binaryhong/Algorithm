str = input()
answer = ""
for i in range(len(str)):
    if str[i].isupper():
        answer+=str[i].lower()
    elif str[i].islower():
        answer+=str[i].upper()
print(answer)
