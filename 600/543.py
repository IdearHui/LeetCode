# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    base = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):
            if not root:
                return 0
            lleft = depth(root.left)
            lright = depth(root.right)
            self.base = max(self.base, lleft + lright)
            return 1 + max(lleft, lright)
        depth(root)
        return self.base
