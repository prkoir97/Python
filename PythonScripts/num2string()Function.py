# A38
# num2string() function

# Function to convert a single-digit number to its corresponding word representation
def num2string(num):
    numString = ""

    # Convert the number to its word representation
    if num == 0:
        numString = "Zero"
    elif num == 1:
        numString = "One"
    elif num == 2:
        numString = "Two"
    elif num == 3:
        numString = "Three"
    elif num == 4:
        numString = "Four"
    elif num == 5:
        numString = "Five"
    elif num == 6:
        numString = "Six"
    elif num == 7:
        numString = "Seven"
    elif num == 8:
        numString = "Eight"
    else:
        numString = "Nine"

    return numString


# Main function
def main():
    # Prompt the user to enter a multi-digit number
    nums = input('Enter a multi-digit number: ')

    # Initialize an empty string to store the word representation of the number
    newStr = ""

    # Iterate over each digit in the input number
    for n in nums:
        # Convert each digit to its corresponding word representation using the num2string function
        word = num2string(int(n))

        # Append the word representation of the digit to the new string
        newStr = newStr + " " + word

    # Construct the final message with the word representation of the entire number
    msg = 'In words, your number is:' + newStr + "."

    # Print the final message
    print(msg)


# Entry point of the program
if __name__ == "__main__":
    main()
