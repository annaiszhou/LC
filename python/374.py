# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(cur_low, cur_high):
            cur_mid = (cur_low + cur_high) / 2
            res = guess(cur_mid)
            if res == 0:
                return cur_mid
            elif res == -1:
                if cur_mid > cur_low:
                    return helper(cur_low, cur_mid)
                else:
                    return helper(cur_low+1, cur_high)
            else:
                if cur_mid > cur_low:
                    return helper(cur_mid, cur_high) 
                else:
                    return helper(cur_mid+1, cur_high)

        res = helper(1, n)
        return res

#Runtime: 32 ms
#Your runtime beats 2.16 % of python submissions.