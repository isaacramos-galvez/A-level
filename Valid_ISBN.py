ISBN = [0,0,0,0,0,0,0,0,0,0,0,0,0]
for count in range(13):
    next_digit = input("Please enter next digit of ISBN")
    ISBN[count] = next_digit

calculated_digit = 0
count = 0
while count < 12:
    calculated_digit = calculated_digit + ISBN[count]
    count = count + 1
    calculated_digit = calculated_digit + ISBN[count * 3]
    count = count + 1

while calculated_digit >= 10:
    calculated_digit = calculated_digit - 10
