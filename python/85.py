class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        res = 0
        for row in matrix:
            for i in xrange(n):
                if row[i] == '1':
                    height[i] = height[i] + 1
                else:
                    height[i] = 0
            stack = [-1]
            for i in xrange(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    res = max(res, h * w)
                stack.append(i)
        return res

#Runtime: 80 ms
#Your runtime beats 99.14 % of python submissions.