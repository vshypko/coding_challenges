# 125
import re


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        s = re.sub('[^A-Za-z0-9]', '', s.lower())
        print(s)

        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                return False

        return True
