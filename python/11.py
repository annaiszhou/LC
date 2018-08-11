class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        res = 0
        while start<end:
        	if height[start]<=height[end]:
        		width = end-start
        		area = width*height[start]
        		res = max(res,area)
        		start+=1
        	else:
        		width = end-start
        		area = width*height[end]
        		res = max(res,area)
        		end-=1
        return res

#Runtime: 40 ms
#Your runtime beats 77.93 % of python submissions.