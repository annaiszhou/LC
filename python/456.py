class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #just a judge and cannot notice the location of 132 pattern
        stack = []
        s3 = -float("inf")
        for n in nums[::-1]:
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False

#Runtime: 36 ms
#Your runtime beats 100.00 % of python submissions.