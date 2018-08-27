class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        res = 0
        toCheck = {n}
        while toCheck:
            res += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return res
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp
        return res 

#Runtime: 332 ms
#Your runtime beats 75.76 % of python submissions.