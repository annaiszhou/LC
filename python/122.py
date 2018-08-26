class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
        	return 0
        total = 0
        for i in range(len(prices)):
        	if i+1<len(prices) and prices[i+1]>prices[i]:
        		total += prices[i+1]-prices[i]
        return total
        
#Runtime: 60 ms
#Your runtime beats 18.40 % of python3 submissions.
