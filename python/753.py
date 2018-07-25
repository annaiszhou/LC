class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def dfs(cur, used):
            if len(used) == k**n - 1:
                return [True, cur]
            used.add(cur[-n:])
            for digit in map(str,range(k)):
                new = cur + digit
                if new[-n:] not in used:
                    temp = dfs(new, used)
                    if temp[0]:
                        return temp
                else:
                	new = cur
            used.remove(cur[-n:])
            return [False, cur]

        res = dfs('0'*n, set())[1]
        return res

#Runtime: 60 ms
#Your runtime beats 24.14 % of python submissions.