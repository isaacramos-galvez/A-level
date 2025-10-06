csv_file = 'Computer Science Homework/CSV_file.txt'
file = open(csv_file, 'r')
for line in file:
    data = line.strip().split(',')
    
    name = data[0]
    age = data[1]
    exam1 = data[2]
    exam2 = data[3]
    print(name, age, exam1, exam2)

