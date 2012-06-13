def sum_int_elements_between_min_and_max(mylist):
    
    my_sum = 0
    
    min_element_index = mylist.index(min(mylist))
    max_element_index = mylist.index(max(mylist))
     
    for i in range(min_element_index + 1, max_element_index):
        if isinstance(a[i], int):
            my_sum += a[i]
    return my_sum
a = [1, 2, -100, 3, 4.5, 5, 100, 6, 7, 8]
print sum_int_elements_between_min_and_max(a)