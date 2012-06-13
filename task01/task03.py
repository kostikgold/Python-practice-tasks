def arithmetic_mean_of_positive_after_last_zero(my_list):
    
    last_zero_index = len(my_list) - my_list[::-1].index(0) - 1
    
    positives_sum = 0.
    positives_num = 0 
    
    for i in range(last_zero_index+1, len(a)):
        if (my_list[i]>0):
            positives_sum += my_list[i]; positives_num += 1
    
    if (positives_num != 0):
        return positives_sum/positives_num
    else:
        return None

a = [3, 0, 1, 0, 10, 5, -7, 4, 1]
print arithmetic_mean_of_positive_after_last_zero(a)