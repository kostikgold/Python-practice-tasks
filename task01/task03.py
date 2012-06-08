def arithmeticMeanOfPositiveAfterLastZero(_list):
    last_zero_index = len(a)-a[::-1].index(0)-1
    _sum = 0.; _num = 0 
    for i in range(last_zero_index+1,len(a)):
        if (a[i]>0):
            _sum += a[i]; _num += 1
    if (_num != 0):
        return _sum/_num
    else:
        return "null"

a = [3, 0, 1, 0, 10, 5, -7, 4, 1]
print arithmeticMeanOfPositiveAfterLastZero(a)