# 1.9
class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O() runtime
    # O() space
    def isStringRotation(self, s1, s2):
        if len(s1) != len(s2):
            return False
        return True

    def isSubString(self, s1, s2):
        return s2 in s1


assert Solution().isSubString("waterbottle", "watr") is False
assert Solution().isSubString("waterbottle", "water") is True
# assert Solution().isStringRotation("waterbottl", "erbottlewat") is False
# assert Solution().isStringRotation("waterbottle", "erbottlewat") is True
