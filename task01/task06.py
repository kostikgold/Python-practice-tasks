def swapColumnsWithMinAndMaxEvenElements(_matrix):
    rows = len(_matrix[:])
    columns = len(_matrix[0][:])
    evenNumbersList = []
    for col in xrange(columns):
        evenNumbersInCol = 0
        for row in xrange(rows):
            if _matrix[row][col]%2==0:
                evenNumbersInCol += 1
        evenNumbersList.append(evenNumbersInCol)
    for row in xrange(rows):
        _matrix[row][min(evenNumbersList)], _matrix[row][max(evenNumbersList)] = _matrix[row][max(evenNumbersList)], _matrix[row][min(evenNumbersList)]            
    return _matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
swapColumnsWithMinAndMaxEvenElements(matrix)