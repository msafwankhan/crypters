import string

alphabets = [x for x in string.ascii_lowercase]
numbers = [x for x in range(len(alphabets))]
shift_value = int(input("Enter a shift value for the cipher"))


for _ in range(shift_value):
    buffer = numbers.pop(0)
    numbers.append(buffer)



def caesarcipher(essay):
    new_essay = []
    for word in essay:
        for char in word:
            if char in alphabets:
                new_essay.append(alphabets[numbers.index(alphabets.index(char))])
            else: new_essay.append(char)
    new_essay = "".join(new_essay)
    return new_essay