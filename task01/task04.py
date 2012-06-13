def num_negatives_between_first_zeroes(my_list):
    
    first_zero_index = my_list.index(0)
    second_zero_shift = my_list[first_zero_index+1:len(my_list)-1].index(0)
    second_zero_index = first_zero_index + second_zero_shift + 1
    num_negatives = second_zero_index - first_zero_index-1
    
    return num_negatives

a = [1, 2, 3, 4, 0, 5, 6, 7, 0, 8, 0, 9, 10, 0, 11]
print num_negatives_between_first_zeroes(a)