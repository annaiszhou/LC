class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        pre, cur = 1, 1
        for i in range(2,n):
            pre, cur = cur, pre + cur
        return cur + pre

#Runtime: 20 ms
#Your runtime beats 99.84 % of python submissions.