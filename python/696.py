class Solution(object):
    def resBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, cur, pre = 0, 1, 0
        length = len(s)
        for i in range(1, length):
            if s[i] == s[i-1]:
                cur += 1
            else:
                res += min(pre, cur)
                pre = cur
                cur = 1
        res += min(pre, cur)
        return res

#Runtime: 124 ms
#Your runtime beats 73.87 % of python submissions.