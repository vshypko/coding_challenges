# 1.3
class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(N) runtime
    # O(1) space
    def urlify(self, s, length):
        listS = list(s)
        for i in range(len(listS)):
            if listS[i] == " ":
                listS[i] = "%20"

        return ''.join(listS)

    # O(N) runtime
    # O(1) space
    def urlifyReplace(self, s, length):
        return s.replace(" ", "%20")


assert (Solution().urlify("Mr John Smith", 13) == "Mr%20John%20Smith")
assert (Solution().urlifyReplace("Mr John Smith", 13) == "Mr%20John%20Smith")
