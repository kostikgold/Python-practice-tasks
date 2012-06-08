def removeZeroesAfterMax(_list):
    maxElementIndex = _list.index(max(_list))
    finished = False
    while not finished:
        for i in xrange(maxElementIndex, len(_list)):
            if (_list[i]==0):
                _list.pop(i)
                break            
        if (i==len(_list)-1):
            finished = True             
    return _list
a = [1, 2, 3, 4, 100, 0, 0, 0, 6]
print removeZeroesAfterMax(a)