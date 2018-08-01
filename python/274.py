class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        s, n = sorted(citations)[::-1], len(citations)
        if not s or s[0]==0: return 0
        if len(citations)==1: return 1
        for i in range(n):
            if s[i]<=i:
                return i
        return n        

#Runtime: 36 ms
#Your runtime beats 7.48 % of python submissions.