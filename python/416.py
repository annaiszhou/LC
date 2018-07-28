class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(n, target):
            if target == 0:
                return True
            elif target < 0 or n == 0:
                return False
            elif memory[n][target] is not None:
                return memory[n][target]
            not_used = helper(n-1, target)
            used = helper(n-1, target - nums[n-1])
            res = not_used or used
            memory[n][target] = res
            return res
        
        if sum(nums)%2!=0:
            return False
        else:
            total = sum(nums)/2
            memory = [[None for j in range(total+1)] for i in range(len(nums)+1)]
            return helper(len(nums), total)

#Runtime: 2696 ms
#Your runtime beats 3.04 % of python submissions.