# 1.6
class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(N) runtime
    # O(N) space
    def stringCompression(self, s):
        if len(s) <= 0:
            return s

        compressedString = ""
        counter = 1

        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                counter += 1
            if s[i] != s[i+1] or i == len(s) - 2:
                compressedString += s[i] + str(counter)
                counter = 1

        return compressedString if len(compressedString) < len(s) else s


assert (Solution().stringCompression("aabcccccaaa") == "a2b1c5a3")
assert (Solution().stringCompression("abcd") == "abcd")
