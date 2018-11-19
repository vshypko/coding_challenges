# 387
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap.keys():
                hashmap[s[i]] = -1
            else:
                hashmap[s[i]] = i

        for i in range(len(s)):
            if hashmap[s[i]] != -1:
                return i
        return -1
