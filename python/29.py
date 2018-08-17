class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if dividend == -2147483648 and divisor == -1:
            return 2147483648 - 1
        sign = 1
        if dividend < 0:
            if divisor < 0:
                sign = 1
            else:
                sign = -1
        else:
            if divisor < 0:
                sign = -1
            else:
                sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            s = divisor
            val = 1
            while (s + s) <= dividend:
                s = s + s
                val = val + val
            dividend -= s
            res += val
        if sign > 0:
            return res
        else:
            return -res

#Runtime: 44 ms
#Your runtime beats 11.51 % of python submissions.