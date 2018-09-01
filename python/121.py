class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        num, mins=0, prices[0]
        for i in prices:
            if i>mins:
                num = max(num,i-mins)
            else:
                mins = i
        return num
        
#Runtime: 44 ms
#Your runtime beats 9.83 % of python submissions.