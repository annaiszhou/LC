class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        reserved_s = s [::-1]
        l = len(reserved_s)
        dict_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = dict_roman[reserved_s[0]]
        for i in range(1,l):
            a, b = dict_roman[reserved_s[i]], dict_roman[reserved_s[i-1]]
            if a < b:
                res -= a
            else:
                res += a
        return res

#Runtime: 80 ms
#Your runtime beats 87.60 % of python submissions.