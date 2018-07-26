class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=count=9
        while count < n:
            i *= 10
            count += i * len(str(i))
        extra = n - (count-i*len(str(i)))
        div, mod = divmod(extra, len(str(i)))
        if mod == 0:
            target = ((i//9-1)+div)
            return int(str(target)[-1])
        else:
            target = (i//9+div)
            return int(str(target)[mod-1])

#Runtime: 20 ms
#Your runtime beats 100.00 % of python submissions.