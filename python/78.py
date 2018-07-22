class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in nums:
            if not res:
                res.append([i])
            else:
                for j in range(len(res)):
                    res.append(res[j]+[i])
                res.append([i])
        res.append([])
        return res

#Runtime: 28 ms
#Your runtime beats 96.83 % of python submissions.