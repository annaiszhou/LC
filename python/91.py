class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        n = len(s)
        sums = [0 for _ in range(n+1)]
        sums[0] = sums[1] = 1
        for i in range(1, n):
            v1 = int(s[i:i+1])
            v2 = int(s[i-1:i+1])
            if 0 < v1 <= 9:
                sums[i+1] = sums[i]
            if 10 <= v2 <= 26:
                sums[i+1] += sums[i-1]
            if sums[i+1] == 0:
                return 0
        res = sums[n]
        return res

#Runtime: 44 ms
#Your runtime beats 7.48 % of python submissions.