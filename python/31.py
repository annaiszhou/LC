class Solution:
    def nextpermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        change, l = False, len(nums) - 2
        while 0 <= l:
            r = len(nums) - 1  
            while l < r and nums[r] <= nums[l]: 
            	r -= 1
            if r <= l: 
            	l -= 1
            else: 
            	nums[l], nums[l + 1:], change = nums[r], sorted(nums[l + 1:r] + [nums[l]] + nums[r + 1:]), True
            	break
        if not change: nums.sort()

#Runtime: 48 ms
#Your runtime beats 98.86 % of python3 submissions.