# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def helper(vals):
            if not vals:
                return [None]
            if len(vals) == 1:
                return [TreeNode(vals[0])]
            nodeList = []
            for i in range(len(vals)):
                leftside = helper(vals[0:i])
                rightside = helper(vals[i+1:])
                for l in leftside:
                    for r in rightside:
                        node = TreeNode(vals[i])
                        node.left = l
                        node.right = r
                        nodeList.append(node)
            return nodeList
        
        if n == 0:
            return []
        vals = [i for i in range(1,n+1)]
        res = helper(vals)
        return res

#Runtime: 80 ms
#Your runtime beats 6.87 % of python submissions.