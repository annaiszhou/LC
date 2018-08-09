# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(postorder.pop())
            ind = inorder.index(root.val)
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root

    '''
    def buildTree(self, inorder, postorder):
        self.inorder = inorder
        self.postorder = postorder
        self.indDict = {val: i for i, val in enumerate(self.inorder)}
        return self.helper(0, len(inorder))
    
    def helper(self, leftInd, rightInd):
        if leftInd < rightInd:
            root = TreeNode(self.postorder.pop())
            rootInd = self.indDict[root.val]
            root.right = self.helper(rootInd+1, rightInd)
            root.left = self.helper(leftInd, rootInd)
            return root
    '''

    '''
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
            
        root = TreeNode(postorder[-1])
        stack = [root]
        i, j = len(postorder)-2, len(inorder) - 1
        while i >= 0:
            node = TreeNode(postorder[i])
            tmp = None
            while stack and stack[-1].val == inorder[j]:
                tmp = stack.pop()
                j -= 1
            if tmp:
                tmp.left = node
            else:
                stack[-1].right = node
            
            stack.append(node)
            i -= 1
        return root
    '''

#Runtime: 136 ms
#Your runtime beats 54.33 % of python submissions.