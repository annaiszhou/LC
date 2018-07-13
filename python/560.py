class Solution:
    def sbarraysm(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
	    count = collections.Counter()
	    count[0] = 1
	    res = s = 0
	    for x in nums:
	        s += x
	        res += count[s-k]
	        count[s] += 1
	    return res

#Runtime: 92 ms
#Your runtime beats 19.22 % of python3 submissions.