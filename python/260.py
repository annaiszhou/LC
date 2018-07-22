class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = set()
        for num in nums:
            if num in stack:
                stack.remove(num)
            else:
                stack.add(num)
        return list(stack)
        
#Runtime: 24 ms
#YYour runtime beats 100.00 % of python submissions.