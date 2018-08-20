# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def depth(p):
            if not p:
                return 0
            left,right = depth(p.left),depth(p.right)
            self.res = max(self.res,left+right)
            return 1+max(left,right)
        
        depth(root)
        return self.res

#Runtime: 36 ms
#Your runtime beats 99.36 % of python submissions.