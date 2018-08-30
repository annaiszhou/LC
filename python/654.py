# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: 
        	return None
        mi,me = self.maxP(nums)
        node = TreeNode(me)
        node.left = self.constructMaximumBinaryTree(nums[:mi])
        node.right = self.constructMaximumBinaryTree(nums[mi+1:])
        return node

    def maxP(self,nums):
        mi,me = 0,nums[0]
        for i,e in enumerate(nums):
            if e > me: 
            	me = e
            	mi = i
        return mi,me

#Runtime: 300 ms
#Your runtime beats 2.06 % of python submissions.