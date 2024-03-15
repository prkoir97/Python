# A48
# Error Checking

age = int(input('Please enter age: '))

while age < 0:
    print('Entered a negative number. Try Again')
    age = int(input('Please enter age: '))

print('You entered your age as:', age)