class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if(len(matrix) == 0):
            return []
        res = [matrix[0][0]];
        i = 0
        j = 0
        reverse = True
        while(i < len(matrix)-1 or j < len(matrix[0])-1):
            if(reverse == True):
                if(i <= 0 and j < len(matrix[0]) - 1):
                    j += 1
                    reverse = False
                elif(j >= len(matrix[0]) - 1):
                    i += 1
                    reverse = False
                else:
                    i -= 1
                    j += 1
            else:
                if(j <= 0 and i < len(matrix) - 1):
                    i += 1
                    reverse = True
                elif(i >= len(matrix) - 1):
                    j += 1
                    reverse = True
                else:
                    i += 1
                    j -= 1           
            if(i < len(matrix) and j < len(matrix[0])):
                res.append(matrix[i][j])
        return res

#Runtime: 144 ms
#Your runtime beats 29.49 % of python submissions.