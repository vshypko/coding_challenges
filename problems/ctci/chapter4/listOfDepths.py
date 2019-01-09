# 4.3
class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# O(N) runtime
# O(N) space
def listOfDepths(root):
    if not root:
        return list()

    result = list()
    currentLevel = list()
    currentLevel.append(root)

    while currentLevel:
        result.append(currentLevel)
        parents = currentLevel
        currentLevel = list()

        for parent in parents:
            if parent.left:
                currentLevel.append(parent.left)
            if parent.right:
                currentLevel.append(parent.right)

    return result


tree = Tree(5)
tree.left = Tree(3)
tree.right = Tree(7)
tree.left.left = Tree(8)
tree.left.right = Tree(11)
tree.right.left = Tree(13)

# print(listOfDepths(tree))
res = listOfDepths(tree)
for i in res:
    for j in i:
        print(j.data, end=" ")
    print()
