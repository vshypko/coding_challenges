# 4.1
class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(|V| + |E|) runtime
    # O(N) space
    def routeBetweenNodes(self, graph, node1, node2):
        fringe = list()
        visited = set()
        fringe.append(node1)
        while fringe:
            current = fringe.pop()
            if current == node2:
                return True
            if current not in visited:
                visited.add(current)
                for node in graph[current]:
                    fringe.append(node)
        return False


graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
node1 = 'A'
node2 = 'D'

assert Solution().routeBetweenNodes(graph, node1, node2) is True

node1 = 'B'
node2 = 'A'

assert Solution().routeBetweenNodes(graph, node1, node2) is False
