import time


def nthfib(n):
    if n <= 0:
        return
    if n == 1 or n == 2:
        return 1
    return nthfib(n-1) + nthfib(n-2)


def memoizedNthfib(n, mem=list()):
    if not mem:
        mem = [0] * (n + 1)
    if mem and mem[n]:
        return mem[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = memoizedNthfib(n-1, mem) + memoizedNthfib(n-2, mem)
    mem[n] = result
    return result


n = 33
start = time.time()
print("Regular fib:", nthfib(n))
print("Took %f seconds.\n" % (time.time() - start))
start = time.time()
print("Memoized fib:", memoizedNthfib(n))
print("Took %f seconds." % (time.time() - start))
