# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if node is None: 
                return [0, 0]
            left = helper(node.left)
            right = helper(node.right)
            return node.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1])

        res = helper(root)
        return max(res[0], res[1])     

#Runtime: 76 ms
#Your runtime beats 5.25 % of python submissions.