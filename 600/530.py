# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    Given a binary search tree with non-negative values,
    find the minimum absolute difference between values of any two nodes
    """
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = []

        def bfs(node):
            if node.left:
                bfs(node.left)
            l.append(node.val)
            if node.right:
                bfs(node.right)
        bfs(root)
        return min([abs(l[i] - l[i + 1]) for i in range(len(l) - 1)])
