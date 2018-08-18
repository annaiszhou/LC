class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for num1 in nums1:
        	if num1 in nums2 and num1 not in res:
        		res.append(num1)
        return res

#Runtime: 40 ms
#Your runtime beats 20.64 % of python submissions.