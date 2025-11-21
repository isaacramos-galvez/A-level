def hashing(key):
    sum = 0
    for i in range(len(key)):
        sum = sum + ord(key[i])**2
    return sum % 523

translate = input("Which language do you want to translate from? (english/french)")
if translate == "english":
    english_words = []
    for i in range(523):
        english_words.append("There is no value stored here")

    english_words[hashing("NOW")] = "MAINTENENT"
    english_words[hashing("CAT")] = "CHAT"
    english_words[hashing("PEN")]=  "PLUME"
    print(english_words[hashing(input("INPUT:"))])
    while choice_continue == "yes":
        print(english_words_words[hashing(input("INPUT:"))])
        choice = input("Do you want to continue?")
        if choice == "no":
            choice_continue != "yes"
            break
        else:
            choice_continue = "yes"


elif translate == "french":
    french_words = []
    for i in range(523):
        french_words.append("There is no value stored here")
    
    french_words[hashing("MAINTENENT")] = "NOW"
    french_words[hashing("CHAT")] = "CAT"
    french_words[hashing("PLUME")]=  "PEN"
    choice_continue = "yes"
    while choice_continue == "yes":
        print(french_words[hashing(input("INPUT:"))])
        choice = input("Do you want to continue?")
        if choice == "no":
            choice_continue != "yes"
            break
        else:
            choice_continue = "yes"