class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memory = {}

        def helper(n):
            if n == 0 or n == 1:
                return 1
            num = memory.get(n)
            if num:
                return num
            else:
                num = 0
                for i in range(1, n + 1):
                    num += helper(i - 1) * helper(n-i)
                memory[n] = num
                return num

        return helper(n)

#Runtime: 20 ms
#Your runtime beats 95.25 % of python submissions.