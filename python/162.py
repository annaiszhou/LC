class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        if len(nums) == 2:
        	if nums[0] > nums[1]:
        		return 0
        	else:
        		return 1
        while True:
            if mid == low and mid == high:
                return mid
            elif nums[mid] < nums[mid-1]:
                high = mid - 1
            elif nums[mid] <= nums[mid+1]:
                low = mid + 1
            else:
                return mid
            mid = (low + high) // 2

#Runtime: 20 ms
#Your runtime beats 100.00 % of python submissions.