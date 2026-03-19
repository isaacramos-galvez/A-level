#lempel-ziv compression
message = input("Enter a message with only two different characters e.g. 01101101001010: ")
codebook = {}
encrypt_message = ""
full_char = ""
edit_message = message
index = 1
for char in edit_message:    
    full_char += char
    if char not in codebook:
        codebook[full_char] = index
        index += 1
        full_char = ""

total_char = ""
i = 0
while i < len(message):
    total_char += message[i]
    if i + 1 < len(message):
        next_char = message[i+1]
    else: pass

    if next_char != None:
        combined = total_char + next_char
    else: combined = total_char
    if combined not in codebook or next_char == None:
        add_value = codebook.get(total_char)
        encrypt_message = encrypt_message + str(add_value)
        total_char = ""
    i+=1

print(f"codebook: {codebook}")
print(f"Encoded: {encrypt_message}")