# 207
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}
        visited = [0] * numCourses
        for i in range(numCourses):
            graph[i] = list()

        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(v):
            if visited[v] == -1:
                return False
            elif visited[v] == 1:
                return True
            visited[v] = -1

            for u in graph[v]:
                if not dfs(u):
                    return False
            visited[v] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
