class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 500, 100, 50, 10, 5, 1]
        symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        res = ""
        for i in range(0, len(values), 2):
            d = num // values[i]
            if d < 4:
                res += "".join([symbols[i] for _ in range(d)])
            if d == 4:
                res += symbols[i]+symbols[i-1]
            if d > 4 and d < 9:
                res += symbols[i-1]
                res += "".join([symbols[i] for _ in range(d-5)])
            if d == 9:
                res += symbols[i]+symbols[i-2]
            num = num % values[i]
        return res

#Runtime: 140 ms
#Your runtime beats 6.10 % of python submissions.