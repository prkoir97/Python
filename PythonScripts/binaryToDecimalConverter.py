# A37
# Binary to Decimal Converter

binString = input("Enter binary number: ")

# Initialize a variable to store the decimal equivalent of the binary number
decNum = 0

# Iterate over each character in the binary string
for c in binString:
    # Multiply the current decimal number by 2 to shift it left
    decNum = decNum * 2
    # If the current character is '1', add 1 to the decimal number
    if c == '1':
        decNum = decNum + 1

print("Your number in decimal is: ", decNum)