class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(i, j):
            if (i, j) not in dp:
                if i == j:
                    return nums[i]
                dp[i,j] = max(nums[i]-helper(i+1, j), nums[j]-helper(i, j-1))
            return dp[i,j]

        dp = {}
        res = (helper(0, len(nums)-1) >= 0)
        return res

#Runtime: 44 ms
#Your runtime beats 18.43 % of python submissions.