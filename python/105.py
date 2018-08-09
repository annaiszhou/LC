# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        index = {}
        for i, pre_order in enumerate(preorder):
            index[pre_order] = {}
            index[pre_order]['pre'] = i
        for j, in_order in enumerate(inorder):
            index[in_order]['in'] = j
        self.count = 0
        
        def build(index, inorder, preorder, start, end):
            if start > end: 
                return None
            if start == end:
                self.count += 1
                return TreeNode(inorder[start])
            minindex = self.count
            self.count += 1
            root = TreeNode(preorder[minindex])
            root.left = build(index, inorder, preorder, start, index[preorder[minindex]]['in']-1)
            root.right = build(index, inorder, preorder, index[preorder[minindex]]['in']+1, end)
            return root

        return build(index, inorder, preorder, 0, len(preorder)-1)

#Runtime: 52 ms
#Your runtime beats 89.84 % of python submissions.