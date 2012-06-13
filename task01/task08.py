def removeNonPositiveColumns(my_matrix):
    rows = len(my_matrix)
    columns = len(my_matrix[0])
    removeColumns = []
    
    for col in xrange(columns):
        negativesInColumn = 0
        for row in xrange(rows):
            if my_matrix[row][col]<0:
                negativesInColumn += 1
        if negativesInColumn==rows:
            removeColumns.append(col)
    removedColumns = 0
    
    for col in removeColumns:
        for row in xrange(rows):
            my_matrix[row].pop(col-removedColumns)
        removedColumns += 1
    return my_matrix

matrix = [[1, -2, 3, -4, 5],
          [1, -2, 3, -4, 5],
          [1, -2, 3, -4, 5]]
print removeNonPositiveColumns(matrix)