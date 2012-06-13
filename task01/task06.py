def swapColumnsWithMinAndMaxEvenElements(my_matrix):
    
    rows = len(my_matrix)
    columns = len(my_matrix[0])
    even_numbers_list = []
    
    for col in xrange(columns):
        even_numbers_in_col = 0
        for row in xrange(rows):
            if my_matrix[row][col]%2==0:
                even_numbers_in_col += 1
                
        even_numbers_list.append(even_numbers_in_col)
        
    for row in xrange(rows):
        mr = my_matrix[row]
        min_even_num = min(even_numbers_list)
        max_even_num = max(even_numbers_list)
        
        mr[min_even_num], mr[max_even_num] = mr[max_even_num], mr[min_even_num]
                    
    return my_matrix

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print swapColumnsWithMinAndMaxEvenElements(matrix)