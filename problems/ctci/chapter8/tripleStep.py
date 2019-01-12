# 8.1

# O(N) runtime
# O(N) space
def tripleStep(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    return dp[n]


assert tripleStep(0) == 1
assert tripleStep(1) == 1
assert tripleStep(2) == 2
assert tripleStep(3) == 4
assert tripleStep(4) == 7
