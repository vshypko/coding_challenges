class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversedString = ""
        splitString = s[::-1].split()[::-1]
        for s in splitString:
            reversedString += s + " "

        return reversedString[:-1]
