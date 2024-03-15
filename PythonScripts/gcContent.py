# A11
# GC Content


string = input('Enter a DNA string: ')

length = len(string)
count = 0

for i in string:
    if i == "C":
        count = count + 1

    elif i == "G":
        count = count + 1

    else:
        count = count

result = count / length

print(length)
print(result)