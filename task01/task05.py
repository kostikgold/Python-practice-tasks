def removeZeroesAfterMax(_list):
    maxElementIndex = _list.index(max(_list))
    while(_list.count(0)!=0):
        for i in xrange(maxElementIndex, len(_list)):
            if (_list[i]==0):
                _list.pop(i)
                break
    
    _list.pop(5)
    print _list
             
    return "\r"
a = [1, 2, 3, 4, 100, 0, 0, 0, 6]
#a= [0, 1, 2, 3,   4, 5, 6, 7, 8]
print removeZeroesAfterMax(a)