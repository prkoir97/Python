# A20
# Name Organizer

gl = input('Please enter your list of names: ')

names = gl.split('; ')
print("You Entered: ", names)

for i in names:
    hand = i.split(', ')
    print(hand[1][0] + ". " + hand[0])