class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = set()
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        if nums.count(0) > len(nums)-2:
            return [[0, 0, 0]]
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            while(j < k):
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    l.add((nums[i], nums[j], nums[k]))
                    j += 1
                    continue
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return list(map(list, l))

#Runtime: 1096 ms
#Your runtime beats 37.66 % of python3 submissions.