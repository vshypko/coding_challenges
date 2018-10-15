# 720
class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        sorted_words = sorted(list(set(words)), key=len)
        same_length = list()

        i = 1
        while i <= len(sorted_words):
            result = sorted_words[-i]
            same_length.append(result)
            for k in range(i + 1, len(sorted_words) + 1):
                if len(result) == len(sorted_words[-k]):
                    same_length.append(sorted_words[-k])
                    i += 1
            same_length.sort()
            for word in same_length:
                counter = 0
                for j in range(1, len(word)):
                    if word[0:j] in words:
                        counter += 1
                if counter == len(word) - 1:
                    return word
            same_length.clear()
            i += 1
