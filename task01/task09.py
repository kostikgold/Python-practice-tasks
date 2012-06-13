#DRAFT
import heapq
def insertHalfSumAfterThreeMaxFractions(_list):
    limit = 100
    sortedList = heapq.nlargest(limit, _list)
    sum3 = 0
    counter = 0
    for i in sortedList:
        if i%1!=0:
            sum3 += i
            counter += 1
        if counter == 3:
            break
    print counter, sum3/2
a = [1.1, 2.2, 300.3, 4.4, 500.5, 6.6, 700.7, 8.8, 9.9, 1000]
insertHalfSumAfterThreeMaxFractions(a)