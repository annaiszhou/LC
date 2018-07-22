class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        for num in nums:
        	if num not in stack:
        		stack.append(num)
        	else:
        		stack.remove(num)
        return stack[0]

#Runtime: 856 ms
#Your runtime beats 4.59 % of python submissions.