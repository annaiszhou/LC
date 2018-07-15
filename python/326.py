class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        divide=1
        while divide<=n:
            if divide==n : 
            	return True
            divide*=3
        return False

#Runtime: 156 ms
#Your runtime beats 94.78 % of python submissions.