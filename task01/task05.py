def remove_zeroes_after_max(my_list):
    
    max_element_index = my_list.index(max(my_list))
    finished = False
    
    while not finished:
        for i in xrange(max_element_index, len(my_list)):
            if (my_list[i]==0):
                my_list.pop(i)
                break            
        if (i==len(my_list)-1):
            finished = True             
    return my_list

a = [1, 2, 3, 4, 100, 0, 0, 0, 6]
print remove_zeroes_after_max(a)