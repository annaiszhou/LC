class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in xrange(len(nums)):
            if nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1

#Runtime: 52 ms
#Your runtime beats 26.08 % of python submissions.
