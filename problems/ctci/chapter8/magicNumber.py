# 8.3

# O(log(N)) runtime
# O(1) space
def magicNumber(array):
    return magicNumberHelper(array, 0, len(array) - 1)


def magicNumberHelper(array, start, end):
    if not array or end < start:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return magicNumberHelper(array, mid + 1, end)
    elif array[mid] > mid:
        return magicNumberHelper(array, start, mid - 1)


array = [-7, -3, 0, 3, 5, 12]
print(magicNumber(array))
array = [-7, -3, 0, 4, 5, 12]
print(magicNumber(array))
