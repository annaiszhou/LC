# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """      
        def dfs(root, rightSum):
            if not root:
                return 0 
            right = dfs(root.right, rightSum)
            left = dfs(root.left, rightSum + root.val + right)    
            originalVal = root.val
            root.val = root.val + rightSum + right      
            return originalVal + left + right     

        dfs(root, 0)
        return root

#Runtime: 68 ms
#Your runtime beats 61.40 % of python submissions.