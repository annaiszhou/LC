class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[::-1][k-1]

#Runtime: 24 ms
#Your runtime beats 98.89 % of python submissions.