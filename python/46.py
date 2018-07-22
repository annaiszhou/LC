class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(nums, [])
        return self.res
        
    def helper(self, nums, res):
        if not nums:
            self.res.append(res)
            return
        for num in nums:
            temp = nums[:]
            temp.remove(num)
            self.helper(temp, res[:] + [num])

#Runtime: 40 ms
#Your runtime beats 83.81 % of python submissions.