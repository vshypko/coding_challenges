# 500
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        top_row = set('qwertyuiop')
        middle_row = set('asdfghjkl')
        bottom_row = set('zxcvbnm')

        result = list()

        for word in words:
            counter = 0
            if word[0].lower() in top_row:
                for letter in word:
                    if letter.lower() not in top_row:
                        break
                    else:
                        counter += 1
                if counter == len(word):
                    result.append(word)
            elif word[0].lower() in middle_row:
                for letter in word:
                    if letter.lower() not in middle_row:
                        break
                    else:
                        counter += 1
                if counter == len(word):
                    result.append(word)
            elif word[0].lower() in bottom_row:
                for letter in word:
                    if letter.lower() not in bottom_row:
                        break
                    else:
                        counter += 1
                if counter == len(word):
                    result.append(word)

        return result
