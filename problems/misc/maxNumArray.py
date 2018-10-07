def maxNumArray(A):
    maxVal = float('-inf')
    for item in A:
        if item > maxVal:
            maxVal = item
    return maxVal


print(maxNumArray([1,5,212,63,5231,355,-7753]))
