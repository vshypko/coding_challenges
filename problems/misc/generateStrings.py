def strings(A, n):
    if n == 0:
        return ['']
    result = list()
    for s in strings(A, n-1):
        for c in A:
            result.append(s + c)
    return result


print(strings(['A', 'B', 'C'], 2))
