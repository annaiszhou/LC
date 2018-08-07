class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: Listart[int]
        :rtype: int
        """
        start,end=0,len(nums)-1
        while start<end:
            m=start+(end-start)//2
            if nums[m-1]<nums[m]<nums[m+1]:
                return nums[m]
            elif nums[m-1]<nums[m]:
                if (m-start)%2:
                    end=m-1
                else:
                    start=m+2
            else:
                if (m-1-start)%2:
                    end=m-2
                else:
                    start=m+1
        return nums[start]

#Runtime: 32 ms
#Your runtime beats 9.51 % of python submissions.

