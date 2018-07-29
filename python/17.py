class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def combine(old, next_digit):
            temp = []
            for i in old:
                for j in digit_map[next_digit]:
                    temp.append(i+j)
            return temp

        digit_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        l = len(digits)
        if l == 0:
            return res
        for i in digit_map[digits[0]]:
            res.append(i)
        if l == 1:
            return res
        else:
            i = 1
            while i < l:
                res = combine(res, digits[i])
                i += 1
            return res

#Runtime: 20 ms
#Your runtime beats 100.00 % of python submissions.