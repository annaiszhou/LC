class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets==1:
        	return 0
        if minutesToTest//minutesToDie<=1:
        	return False
        res = 1
        while res > 0:
        	if (1+minutesToTest//minutesToDie)**res>=buckets:
        		return res
        	else:
        		res+=1

#Runtime: 20 ms
#Your runtime beats 91.47 % of python submissions.