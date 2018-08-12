# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#recursively
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
        	return True
        else:
        	return self.helper(root.left,root.right)

    def helper(self,l,r):
        if not l and not r:
        	return True
        if not l or not r:
        	return False
        if l.val == r.val:
        	side1 = self.helper(l.left,r.right)
        	side2 = self.helper(l.right,r.left)
        	return side1 and side2
        else:
        	return False

#Runtime: 24 ms
#Your runtime beats 100.00 % of python submissions.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#iteratively
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
        	return True
        else:
        	stack = [[root.left,root.right]]
        	while stack:
        		leave = stack.pop()
        		leave1 = leave[0]
        		leave2 = leave[1]
        		if not leave1 and not leave2:
        			continue
        		if not leave1 or not leave2:
        			return False
        		if leave1.val == leave2.val:
        			stack.append([leave1.left,leave2.right])
        			stack.append([leave1.right,leave2.left])
        		else:
        			return False
        	return True

#Runtime: 44 ms
#Your runtime beats 5.39 % of python submissions.

