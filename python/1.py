class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(0,len(nums)):
            target1 = target - nums[i]
            if target1 in dict1:
                return sorted([i, dict1[target1]])
            dict1[nums[i]] = i

#Runtime: 20 ms
#Your runtime beats 100.00 % of python submissions.