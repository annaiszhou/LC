class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        gap = float('inf')
        res = 0
        for i in range(len(nums)-2):
            start, end = i+1, len(nums)-1
            while(start<end):
                sums = nums[i]+nums[start]+nums[end]
                if(abs(sums -target)<gap):
                    res = sums
                    gap = abs(sums -target)
                tmp = target - sums
                if tmp>0:
                    start += 1
                elif tmp<0:
                    end -= 1
                else:
                    return target
        return res

#Runtime: 108 ms
#Your runtime beats 73.13 % of python3 submissions.