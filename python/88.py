class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m-1
        pointer2 = n-1
        pointer_res = m+n-1
        while pointer2>=0:
            if nums1[pointer1]>=nums2[pointer2] and pointer1>=0:
                nums1[pointer_res]=nums1[pointer1]
                pointer1-=1
            else:
                nums1[pointer_res]=nums2[pointer2]
                pointer2-=1              
            pointer_res-=1

#Runtime: 24 ms
#Your runtime beats 99.90 % of python submissions.