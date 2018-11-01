# 844
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stackS = list()
        stackT = list()

        for c in S:
            if c == '#':
                if len(stackS) > 0:
                    stackS.pop()
            else:
                stackS.append(c)

        for c in T:
            if c == '#':
                if len(stackT) > 0:
                    stackT.pop()
            else:
                stackT.append(c)

        return ''.join(stackS) == ''.join(stackT)
