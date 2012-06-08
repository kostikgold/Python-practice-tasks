def sumIntElementsBetweenMinAndMax(_list):
    _sum = 0
    for i in range(_list.index(min(_list))+1, _list.index(max(_list))):
        if isinstance(a[i], int):
            _sum += a[i]
    return _sum
a = [1, 2, -100, 3, 4.5, 5, 100, 6, 7, 8]
print sumIntElementsBetweenMinAndMax(a)