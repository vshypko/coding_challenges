# 886
class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        if not dislikes:
            return True

        graph = {}

        for dislike in dislikes:
            if dislike[0] not in graph.keys():
                graph[dislike[0]] = list()
            if dislike[1] not in graph.keys():
                graph[dislike[1]] = list()
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])

        color = {}

        def bfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c

            if node in graph.keys():
                for node in graph[node]:
                    if not bfs(node, abs(c - 1)):
                        return False
            return True

        for node in range(1, N + 1):
            if node not in color:
                if not bfs(node):
                    return False
        return True
