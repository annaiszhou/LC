class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.helper(nums1, nums2, l // 2)
        else:
            return (self.helper(nums1, nums2, l // 2) + self.helper(nums1, nums2, l // 2 - 1)) / 2.   
        
    def helper(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        a_index, b_index = len(a) // 2 , len(b) // 2
        a_value, b_value = a[a_index], b[b_index]
        if a_index + b_index < k:
            if a_value > b_value:
                return self.helper(a, b[b_index + 1:], k - b_index - 1)
            else:
                return self.helper(a[a_index + 1:], b, k - a_index - 1)
        else:
            if a_value > b_value:
                return self.helper(a[:a_index], b, k)
            else:
                return self.helper(a, b[:b_index], k)

#Runtime: 100 ms
#Your runtime beats 95.48 % of python3 submissions.