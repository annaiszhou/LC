class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        res = []
        if row==0:
        	return res
        while matrix:
        	res += matrix.pop(0)
        	if matrix:
        		for x in matrix:
        			if x:
        				res.append(x.pop())
        	else:
        		return res
        	if matrix[-1]:
        		res+=matrix.pop()[::-1]
        	else:
        		return res
        	if matrix:
        		for y in matrix[::-1]:
        			if y:
        				res.append(y.pop(0))
        	else:
        		return res
        return res

#Runtime: 20 ms
#Your runtime beats 100.00 % of python submissions.





