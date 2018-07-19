class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        k_num = set()
        for i in xrange(0, len(nums)):
            if len(k_num) > k:
                k_num.remove(nums[i-k-1])
            if nums[i] in k_num:
                return True
            k_num.add(nums[i])
        return False

#Runtime: 36 ms
#Your runtime beats 73.20 % of python submissions.