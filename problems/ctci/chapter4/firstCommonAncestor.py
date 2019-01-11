# 4.8
class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# O(N) runtime
# O(N) space (call stack)
def firstCommonAncestor(root, p, q):
    if not root or not covers(root, p) or not covers(root, q):
        return None
    return ancestorHelper(root, p, q)


def ancestorHelper(root, p, q):
    if not root or root == p or root == q:
        return root

    pIsOnLeft = covers(root.left, p)
    qIsOnLeft = covers(root.left, q)
    if pIsOnLeft != qIsOnLeft:
        return root
    return ancestorHelper(root.left, p, q) if pIsOnLeft else ancestorHelper(root.right, p, q)


def covers(root, p):
    if not root:
        return False
    if root == p:
        return True
    return covers(root.left, p) or covers(root.right, p)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(9)
root.right.left = TreeNode(4)
root.right.right = TreeNode(7)

assert firstCommonAncestor(root, root.left, root.right.right) == root
assert firstCommonAncestor(root, root, root.right.right) == root
assert firstCommonAncestor(root, root.left.left, root.right.right) == root
assert firstCommonAncestor(root.left, root.left.left, root.left.right) == root.left
assert firstCommonAncestor(None, root.left, root.right) is None
