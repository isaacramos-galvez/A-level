word = input("Enter a word: ")
encrypted_word = ""
index = 0
if len(word) == 1:
    print(word + str(1))
word = word + " "
while word[index+1] != " ":
    count = 0
    while word[index] == word[index+1]:
        count += 1
        index += 1
    encrypted_word = encrypted_word + word[index] + str(count + 1)
    print(encrypted_word)
    break
print(encrypted_word)