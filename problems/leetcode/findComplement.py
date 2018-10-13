class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        complement = bin(num ^ 0xffffffff)[-(len(bin(num))-2):]
        return int(complement, 2)
