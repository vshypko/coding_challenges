# 345
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        index = []
        seen = []
        word = list(s)
        for i in range(len(s)):
            if word[i].lower() in vowels:
                index.append(i)
                seen.append(word[i])
        for i in range(len(seen)):
            word[index[i]] = seen[len(seen) - i - 1]
        return ''.join(word)
