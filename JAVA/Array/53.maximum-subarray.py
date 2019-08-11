#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# O(n)
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max = -float('INF')
#         sum = -float('INF')
#         for num in nums:
#             if num>=sum+num:
#                 sum = num
#             else:
#                 sum = sum+num
#             if sum>max:
#                 max = sum
#             # print(max)
#         return max

# divide and conquer
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.divideAndConquer(nums,0,len(nums)-1)

    def divideAndConquer(self,nums,l,r):
        if l>=r:
            return nums[l]
        mid = int(l+(r-l)/2)
        left = self.divideAndConquer(nums,l,mid)
        right = self.divideAndConquer(nums,mid+1,r)
        leftMax = nums[mid]
        rightMax = nums[mid+1]
        temp = 0
        for i in range(l,mid+1)[::-1]:
            # print(l,i,mid)
            temp += nums[i]
            if temp>leftMax:
                leftMax = temp
        temp = 0
        for i in range(mid+1,r+1):
            # print(mid+1,i,r)
            temp += nums[i]
            if temp>rightMax:
                rightMax = temp
        print(l,mid,r,left,right,leftMax,rightMax)
        return max(left,right,leftMax+rightMax)




