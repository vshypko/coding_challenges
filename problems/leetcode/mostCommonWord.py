# 819
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        punctuation = "!()-[]{};:\'\",<>./?@#$%^&*_~"
        hashmap = {}
        listParagraph = list(paragraph)

        for i in range(len(listParagraph)):
            if listParagraph[i] in punctuation:
                listParagraph[i] = " "

        words = ''.join(listParagraph).lower().split()

        for word in words:
            if word not in banned:
                if word not in hashmap.keys():
                    hashmap[word] = 0
                hashmap[word] += 1

        maxVal = float('-inf')
        maxWord = ""
        for k, v in hashmap.items():
            if v > maxVal:
                maxVal = v
                maxWord = k

        return maxWord
