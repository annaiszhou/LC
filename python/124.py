class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None

        def helper(root):
            if not root:
                return -float('inf'), -float('inf')
            if not root.left and not root.right:
                return root.val, root.val
            left_max, left_sum = helper(root.left)
            right_max, right_sum = helper(root.right)
            max_sum = max(root.val, root.val + left_sum, root.val + right_sum)             
            return max(left_max, right_max, max_sum, root.val + left_sum + right_sum), max_sum

        max_seen, max_sum = helper(root)
        return max(max_seen, max_sum)

#Runtime: 100 ms
#Your runtime beats 99.02 % of python3 submissions.