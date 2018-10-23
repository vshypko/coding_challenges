# 1.9
class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(len(s1) + len(s2)) runtime
    # O(len(s2)) space
    def isStringRotation(self, s1, s2):
        if len(s1) != len(s2):
            return False
        return self.isSubString(s1, s2 + s2)

    def isSubString(self, s1, s2):
        return s1 in s2


assert Solution().isSubString("waterbottle", "watr") is False
assert Solution().isSubString("waterbottle", "water") is True
assert Solution().isStringRotation("waterbottl", "erbottlewat") is False
assert Solution().isStringRotation("waterbottle", "erbottlewat") is True
