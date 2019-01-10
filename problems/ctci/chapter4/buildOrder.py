# 4.7

# O() runtime
# O() space

class Graph:
    def __init__(self, vertices, edges):
        self.graph = {}
        self.addVertices(vertices)
        self.addEdges(edges)
        self.V = self.graph.keys()

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def addEdges(self, edges):
        for u, v in edges:
            self.addEdge(u, v)

    def addVertices(self, vertices):
        for v in vertices:
            self.graph[v] = list()

    def topologicalSortHelper(self, v, visited, stack):
        visited.add(v)

        for u in self.graph[v]:
            if u not in visited:
                self.topologicalSortHelper(u, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):
        visited = set()
        stack = list()

        for v in self.V:
            if v not in visited:
                self.topologicalSortHelper(v, visited, stack)

        print(stack)
        return stack


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

g = Graph(projects, dependencies)
print(g.graph)
g.topologicalSort()

# graph = {}
# for p in projects:
#     graph[p] = list()
#
# for u, v in dependencies:
#     graph[u].append(v)
#
# print(graph)
#
#
# def topologicalSort(graph, start):
#     visited = set()
#     stack = list()
#     order = list()
#
#     queue = [start]
#     while queue:
#         v = queue.pop()
#         if v not in visited:
#             visited.add(v)
#             queue.extend(graph[v])
#
#             while stack and v not in graph[stack[-1]]:
#                 order.append(stack.pop())
#             stack.append(v)
#
#     return stack + order[::-1]
#
# print(topologicalSort(graph, 'a'))
