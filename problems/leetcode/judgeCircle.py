# 657
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        horizontalCounter = 0
        verticalCounter = 0
        for move in moves:
            if move == 'U':
                verticalCounter += 1
            elif move == 'D':
                verticalCounter -= 1
            elif move == 'R':
                horizontalCounter += 1
            elif move == 'L':
                horizontalCounter -= 1
        return horizontalCounter == verticalCounter == 0
