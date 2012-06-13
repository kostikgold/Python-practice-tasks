def increase_diag_element_by_column_minimum(_matrix):
    rows = len(_matrix)
    columns = len(_matrix[0])
    
    for col in xrange(columns):
        elementsInColumn = []
        for row in xrange(rows):
            elementsInColumn.append(_matrix[row][col])
        _matrix[col][col] += min(elementsInColumn)
    
    return _matrix        

matrix = [[1,10,100],
          [2,20,200],
          [3,30,300]]
print increase_diag_element_by_column_minimum(matrix)