class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memory = [1 for i in range(len(nums)+1)]
        for num in nums:
            memory[num]-=1
        return memory.index(1)

#Runtime: 44 ms
#Your runtime beats 20.04 % of python submissions.