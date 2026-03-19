word1 = input("Enter word1: ")
word2 = input("Enter word2: ")
in_word = False
for i in range(len(word1)):
    if word1[i] in word2: 
        in_word = True
        word2 = word2.replace(word1[i], "", 1)
    elif word1[i] not in word2: 
        in_word = False
        break
if in_word == True: print("The word can be found. ")
elif in_word == False: print("The word cannot be found. ")