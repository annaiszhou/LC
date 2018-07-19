# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()
        queue.append(root)
        res = []
    
        while queue:
            length = len(queue)
            temp = []
            for i in range(length):
                node = queue.pop()
                if node:
                    temp.append(node.val)
                    queue.appendleft(node.left)
                    queue.appendleft(node.right)
            if temp != []:
                res.append(temp)
            
        return res

#Runtime: 28 ms
#Your runtime beats 87.86 % of python submissions.