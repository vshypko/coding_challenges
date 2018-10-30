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

        return sorted(s1) == sorted(s2)

    # O(N) runtime
    # O(1) space
    def isPermutationAuthor(self, s1, s2):
        if len(s1) != len(s2):
            return False

        letters = [0] * 256  # ASCII

        for c in s1:
            letters[ord(c)] += 1

        for c in s2:
            letters[ord(c)] -= 1
            if letters[ord(c)] < 0:
                return False

        return sum(letters) == 0


assert (Solution().isPermutation("abcd", "bcda") is True)
assert (Solution().isPermutation("fadc", "zxwq") is False)
assert (Solution().isPermutation("fadc", "adc") is False)

assert (Solution().isPermutationSorted("abcd", "bcda") is True)
assert (Solution().isPermutationSorted("fadc", "zxwq") is False)
assert (Solution().isPermutationSorted("fadc", "adc") is False)

assert (Solution().isPermutationAuthor("abcd", "bcda") is True)
assert (Solution().isPermutationAuthor("fadc", "zxwq") is False)
assert (Solution().isPermutationAuthor("fadc", "adc") is False)
