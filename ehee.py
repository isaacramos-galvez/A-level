def sort_array(source_array):
    value = 0
    odd_list = []
    for i in source_list:
        if i % 2 == 1:
            odd_list.append(i)
    for j in odd_list:
        if odd_list[j] > odd_list[j+1]:
            temp = odd_list[j]
            odd_list[j] = odd_list[j+1]
            odd_list[j+1] = temp
    for k in source_list:
        if k % 2 == 1:
            source_list[k] = odd_list[value]
            value += 1

