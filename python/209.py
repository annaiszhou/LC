class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res=float("inf")
        left=0
        a=0
        for i in range(len(nums)):
            a+=nums[i]
            while a>=s:
                res=min(i-left+1,res)
                a-=nums[left]
                left+=1
        if res!=float("inf"):
            return res 
        else:
            return 0  

#Runtime: 28 ms
#Your runtime beats 98.07 % of python submissions.