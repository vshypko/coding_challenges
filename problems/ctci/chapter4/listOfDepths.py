# 4.3
class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O() runtime
    # O() space
    def listOfDepths(self, tree):
        if not tree:
            return 0



tree = Tree(5)
tree.left = Tree(3)
tree.right = Tree(7)
print(Solution().listOfDepths(tree))
