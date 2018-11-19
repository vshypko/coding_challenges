# 151
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splitted = s.split()
        for s in splitted:
            s = s.strip()
        if len(splitted) == 0 or s == '':
            return ''
        for i in range(len(splitted) // 2):
            splitted[i], splitted[len(splitted) - i - 1] = splitted[len(splitted) - i - 1], splitted[i]
        return ' '.join(splitted)
