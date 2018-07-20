class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            if target == 0:
                return False
        m, n = len(matrix), len(matrix[0])-1
        r = 0
        while r < m and n >= 0:
            if matrix[r][n] == target:
                return True
            if matrix[r][n] > target:
                n -= 1
            else: 
                r += 1
        return False   

#Runtime: 76 ms
#Your runtime beats 36.57 % of python submissions.

'''
#divide and conquer
	def helper(matrix, rowStart, rowEnd, colStart, colEnd, target):
            if(rowStart > rowEnd) | (colStart > colEnd):
                return False
            rowMid = (rowStart + rowEnd) // 2
            colMid = (colStart + colEnd) // 2
            if(matrix[rowMid][colMid] == target):
                return True
            elif (matrix[rowMid][colMid] > target):
                return helper(matrix, rowStart, rowMid - 1, colStart, colMid - 1, target) | helper(matrix, rowMid, rowEnd, colStart, colMid - 1, target) | helper(matrix, rowStart, rowMid - 1, colMid - 1, colEnd, target)
            else:
                return helper(matrix, rowMid + 1, rowEnd, colMid + 1, colEnd, target) | helper(matrix, rowMid + 1, rowEnd, colStart, colMid, target)| helper(matrix, rowStart, rowMid, colMid + 1, colEnd, target)

        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return False
	row, col = len(matrix), len(matrix[0])
        return helper(matrix, 0, row - 1, 0, col - 1, target)
		
#Runtime: 892 ms
#Your runtime beats 1.69 % of python submissions.
'''