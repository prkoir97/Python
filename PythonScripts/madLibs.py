# A11
# Mad Libs

sentence = ("If it word1 like a word2 and word3 like a word2, it probably is a word2.")

N1 = input('Enter a noun: ')
sentence = sentence.replace("word2",N1)
V1 = input('Enter a verb: ')
sentence = sentence.replace("word1",V1)
V2 = input('Enter another verb: ')
sentence = sentence.replace("word3",V2)

print("New Sentence:")
print(sentence)