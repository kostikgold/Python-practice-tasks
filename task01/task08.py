def removeNonPositiveColumns(_matrix):
    rows = len(_matrix[:])
    columns = len(_matrix[0][:])
    removeColumns = []
    for col in xrange(columns):
        negativesInColumn = 0
        for row in xrange(rows):
            if _matrix[row][col]<0:
                negativesInColumn += 1
        if negativesInColumn==rows:
            removeColumns.append(col)
    removedColumns = 0
    for col in removeColumns:
        for row in xrange(rows):
            _matrix[row].pop(col-removedColumns)
        removedColumns += 1
    return _matrix
matrix = [[1, -2, 3, -4, 5],
          [1, -2, 3, -4, 5],
          [1, -2, 3, -4, 5]]
print removeNonPositiveColumns(matrix)