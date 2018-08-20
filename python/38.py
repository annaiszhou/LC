class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for ns in range(n-1):
            prev = res
            res = ''
            j = 0
            while j < len(prev):
                cur = prev[j]
                cnt = 1
                j += 1
                while j < len(prev) and prev[j] == cur:
                    cnt += 1
                    j += 1
                res += str(cnt) + str(cur)
        return res

#Runtime: 28 ms
#Your runtime beats 40.01 % of python submissions.