word = input("What are you looking for?")
vector = ["Cat","Dog","Monkey"]
for i in range(len(vector)):
    if vector[i] == "":
        print("The word is not in the list")
        break
    if word == vector[i]:
        print("The word is at index",i + 1)
        break
    

