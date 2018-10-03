def nthfib(n):
    if n <= 1:
        return 1
    return nthfib(n-1) + nthfib(n-2)

print(nthfib(1))
print(nthfib(5))
print(nthfib(10))
