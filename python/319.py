class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 1
        
        while i < n + 1:
            if i ** 2 <= n:
                count += 1
            else:
                break
            
            i += 1
        return count

#Runtime: 20 ms
#Your runtime beats 91.62 % of python submissions.