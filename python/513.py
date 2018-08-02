# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [-1, 0]
        self.dfs(root, res, 0)
        return res[1]

    def dfs(self, root, res, level):
        if not root:
            return
        if level > res[0]:
            res[0], res[1] = level, root.val
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)

#Runtime: 40 ms
#Your runtime beats 74.33 % of python submissions.