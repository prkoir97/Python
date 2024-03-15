# A8
# Encrypted Message: prints out encrypted message of user input

word = input('Enter Message Here:')
codedWord = ""
for ch in word:
    offset = ord(ch) - ord('a') + 13
    wrap = offset % 26
    newChar = chr(ord('a') + wrap)
    codedWord = codedWord + newChar

print("The coded word (with wrap) is", codedWord)