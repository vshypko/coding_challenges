# 4.9
import copy


class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# O() runtime
# O() space
def bstSequences(node):
    results = list()
    if not node:
        results.append(list())
        return results
    prefix = list()
    prefix.append(node.data)
    leftSeq = bstSequences(node.left)
    rightSeq = bstSequences(node.right)
    for left in leftSeq:
        for right in rightSeq:
            weaved = list()
            weaveLists(left, right, weaved, prefix)
            results.extend(weaved)
    return results


def weaveLists(first, second, results, prefix):
    if len(first) == 0 or len(second) == 0:
        result = copy.deepcopy(prefix)
        if first:
            result.extend(first)
        if second:
            result.extend(second)
        results.append(result)
        return

    headFirst = first.pop(0)
    prefix.append(headFirst)
    weaveLists(first, second, results, prefix)
    del prefix[-1]
    first.insert(0, headFirst)

    headSecond = second.pop(0)
    prefix.append(headSecond)
    weaveLists(first, second, results, prefix)
    del prefix[-1]
    second.insert(0, headSecond)


tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right = TreeNode(3)

threeNodesSeq = bstSequences(tree)
assert [2, 1, 3] in threeNodesSeq
assert [2, 3, 1] in threeNodesSeq

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

assert bstSequences(None) == [[]]
sequences = bstSequences(root)
assert [5, 3, 8, 1, 4, 6, 9] in sequences
assert [5, 8, 3, 1, 4, 6, 9] in sequences
