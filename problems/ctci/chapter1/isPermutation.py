# 1.2
class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(N) runtime
    # O(N) space
    def isPermutation(self, s1, s2):
        if len(s1) != len(s2):
            return False

        hashmap1, hashmap2 = {}, {}
        counter = 0

        for c in s1:
            if c not in hashmap1.keys():
                hashmap1[c] = 1
            else:
                hashmap1[c] += 1

        for c in s2:
            if c not in hashmap2.keys():
                hashmap2[c] = 1
            else:
                hashmap2[c] += 1

        for key in hashmap1.keys():
            if key in hashmap2.keys():
                if hashmap1[key] == hashmap2[key]:
                    counter += 1

        return counter == len(s2)

    # O(Nlog(N)) runtime
    # O(1) space
    def isPermutationSorted(self, s1, s2):
        if len(s1) != len(s2):
            return False

        sortedS1 = sorted(s1)
        sortedS2 = sorted(s2)

        for i in range(len(s1)):
            if sortedS1[i] != sortedS2[i]:
                return False

        return True


assert (Solution().isPermutation("abcd", "bcda") is True)
assert (Solution().isPermutation("fadc", "zxwq") is False)
assert (Solution().isPermutation("fadc", "adc") is False)

assert (Solution().isPermutationSorted("abcd", "bcda") is True)
assert (Solution().isPermutationSorted("fadc", "zxwq") is False)
assert (Solution().isPermutationSorted("fadc", "adc") is False)
