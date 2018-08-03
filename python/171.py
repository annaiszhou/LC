class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        res = 0
        for i in range(0,length):
            temp = ord(s[i])-ord('A')+1
            res = 26*res +temp
        return res

#Runtime: 28 ms
#Your runtime beats 84.31 % of python submissions.