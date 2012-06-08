def numNegativesBetweenFirstZeroes(_list):
    firstZeroIndex =_list.index(0)
    secondZeroIndex = firstZeroIndex + _list[firstZeroIndex+1:len(_list)-1].index(0) + 1
    _sum = 0
    for i in xrange(firstZeroIndex+1,secondZeroIndex):
        _sum += a[i]
    return _sum
a = [1, 2, 3, 4, 0, 5, 6, 7, 0, 8, 0, 9, 10, 0, 11]
print numNegativesBetweenFirstZeroes(a)