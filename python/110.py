# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        depth, res = self.helper(root, 0)
        return res

    def helper(self, root, depth):
        if not root:
            return depth, True
        depth1 = depth2 = depth
        res1 = res2 = True
        if root.left:
            depth1, res1 = self.helper(root.left, depth + 1)
        if root.right:
            depth2, res2 = self.helper(root.right, depth + 1)
        if not res2 or not res1:
            return max(depth1, depth2), False
        return max(depth1, depth2), abs(depth2 - depth1) <= 1

#Runtime: 44 ms
#Your runtime beats 79.17 % of python submissions.
