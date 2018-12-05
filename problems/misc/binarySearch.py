def binarySearchIterative(array, num):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == num:
            return True
        elif array[mid] < num:
            start = mid + 1
        elif array[mid] > num:
            end = mid - 1

    return False


def binarySearchRecursive(array, num):
    if len(array) == 0:
        return False

    mid = len(array) // 2
    if array[mid] == num:
        return True
    elif array[mid] < num:
        return binarySearchRecursive(array[mid+1:], num)
    elif array[mid] > num:
        return binarySearchRecursive(array[:mid], num)


if __name__ == '__main__':
    print("Iterative:")
    print(binarySearchIterative([1, 5, 6, 7, 8, 10, 15], 3))
    print(binarySearchIterative([1, 5, 6, 7, 8, 10, 15], 6))
    print(binarySearchIterative([1, 5, 6, 7, 8, 10, 15], 15))
    print(binarySearchIterative([1, 5, 6, 7, 8, 10, 15], 1))
    print(binarySearchIterative([1, 5, 6, 7, 8, 10, 15], 17))
    print("\nRecursive:")
    print(binarySearchRecursive([1, 5, 6, 7, 8, 10, 15], 3))
    print(binarySearchRecursive([1, 5, 6, 7, 8, 10, 15], 6))
    print(binarySearchRecursive([1, 5, 6, 7, 8, 10, 15], 15))
    print(binarySearchRecursive([1, 5, 6, 7, 8, 10, 15], 1))
    print(binarySearchRecursive([1, 5, 6, 7, 8, 10, 15], 17))
