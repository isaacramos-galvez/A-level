def merge_list(left_half, right_half, numbers): 
    index1 = index2 = 0
    while index1 + index2 < len(numbers):
        if index2 == len(right_half) or (index1 < len(left_half) and left_half[index1] < right_half[index2]):
            numbers[index1 + index2] = left_half[index1]
            index1 += 1
        else:
            numbers[index1 + index2] = right_half[index2]
            index2 += 1
        

def merge_sort(numbers):
    length = len(numbers)
    middle = length // 2
    if length < 2:
        return 
    left_half = numbers[:middle]
    right_half = numbers[middle:]
    merge_sort(left_half)
    merge_sort(right_half)
    merge_list(left_half, right_half, numbers)


list_sort = [10,9,8,7,6,5,4,5,6,7,3,2,7,1,8,0]
print(list_sort)
merge_sort(list_sort)
print(list_sort)

    