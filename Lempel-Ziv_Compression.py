#lempel-ziv compression
message = input("Enter a message with only two different characters e.g. 01101101001010: ")
codebook = {}
index = 1
encrypt_message = ""
full_char = ""
edit_message = message
for char in edit_message:    
    full_char += char
    if char not in codebook:
        codebook.update({char: index})
        index += 1
    else:
        if full_char not in codebook:
            codebook.update({full_char: index})
            index+=1
            full_char = ""
    
        
    print(char)
    print(full_char)
    print(codebook)

full_char = ""
for new_char in message:
    full_char = full_char + new_char
    if full_char in codebook:
        pass
    elif full_char not in codebook:
        full_char = new_char[:len(full_char)-1]
        if codebook.get(full_char) == None:
            encrypt_message = encrypt_message + str(codebook.get(char))
            full_char = ""
        elif codebook.get(char) == None:
            encrypt_message = encrypt_message + str(codebook.get(full_char))
            full_char = ""
        
    
    print(new_char)
    print(full_char)
    print(encrypt_message)
    
print(encrypt_message)