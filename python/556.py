class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        number = [c for c in str(n)]
        for l in range(len(number) - 2, -1, -1):
            r = len(number) - 1
            while l < r and number[r] <= number[l]:
                r -= 1
            if l != r:
                number[l], number[r] = number[r], number[l]
                number[l + 1:] = sorted(number[l + 1:])
                num = int("".join(number))
                return num if -2 ** 31 <= num <= 2 ** 31 - 1 else -1
        return -1

#Runtime: 24 ms
#Your runtime beats 15.58 % of python submissions.