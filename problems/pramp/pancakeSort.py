def pancakeSort(arr):
    if not arr:
        return arr

    n = len(arr)
    startIndex = 0

    for j in range(n):
        maxElem = float('-inf')
        maxElemIndex = 0
        for i in range(len(arr) - startIndex):
            maxElem = max(maxElem, arr[i])
            if maxElem == arr[i]:
                maxElemIndex = i + 1

        arr = flip(arr, maxElemIndex)
        arr = flip(arr, len(arr) - startIndex)
        startIndex += 1

    return arr


def flip(arr, k):
    return arr[:k][::-1] + arr[k:]


assert pancakeSort([1, 3, 1]) == [1, 1, 3]
assert pancakeSort([1, 3, 2, 5, 4]) == [1, 2, 3, 4, 5]
