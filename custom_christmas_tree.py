def custom_christmas_tree(chars, n):

    tree_list = []
    char_list = []
    char = len(chars)
    bauble_number = 0
    count = 0

    for i in range(char):
        char_list.append(chars[count])
        count += 1

    for i in range(n):
        layer = ""
        index = bauble_number % char
        layer = layer + str(char_list[index])
        bauble_number += 1
        print(layer)
    
custom_christmas_tree("%^", 10)
