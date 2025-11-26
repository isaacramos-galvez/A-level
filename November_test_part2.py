word1 = input("Enter a word")
word2 = input("Enter a second word")

word1_list = []
for i in range(len(word1)):
    list.append(word1)

letters1 = []
for i in range(26):
    letters1.append(0) # Create a list with a 0 for each letter of the alphabet

index1 = 0
index2 = 0
count1 = 0

list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(len(word1)):
    if word1_list[index2] == list[index1]:
        letters1[word1_list[index1]] += 1 #  Adds a one to the index of the list of the alphabet if this letter is found
    elif word1_list[index2] != list[index1]:
        index1 += 1 

index3 = 0
index4 = 0
count2 = 0
letters2 = []

for i in range(26):
    letters2.append(0) # Create a list with a 0 for each letter of the alphabet
  
list2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(len(word1)):
    if word2_list[index2] == list[index1]:
        letters1[word1_list[index]] += 1 #  Adds a one to the index of the list of the alphabet if this letter is found
    elif word1_list[index2] != list[index1]:
        index1 += 1 



if len(word1) > len(word2):
    print("The first word cannot be formed from the second word as the first word is longer.")

