class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums))!=len(nums):
        	return True
        else:
        	return False

#Runtime: 28 ms
#Your runtime beats 99.95 % of python submissions.