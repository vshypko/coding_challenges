# 210
class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {}

        isCycle = False

        for i in range(numCourses):
            graph[i] = list()

        for u, v in prerequisites:
            graph[v].append(u)

        color = [Solution.WHITE] * numCourses
        order = list()

        def dfs(node):
            nonlocal isCycle

            if isCycle:
                return

            color[node] = Solution.GRAY

            if node in graph.keys():
                for neighbor in graph[node]:
                    if color[neighbor] == Solution.GRAY:
                        isCycle = True
                        return
                    elif color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
            color[node] = Solution.BLACK
            order.append(node)

        for v in graph.keys():
            if color[v] == Solution.WHITE:
                dfs(v)

        return order[::-1] if not isCycle else []
