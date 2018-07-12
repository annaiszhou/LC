class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.table = [['.' for j in range(n)] for i in range(n)]
        self.solution = []
        self.begin_position(0)
        return self.solution
    
    def begin_position(self,row_index):
        flag = False
        for i in range(self.n):
            if self.check_position(row_index,i):
                self.table[row_index][i] = 'Q'
                if row_index == self.n-1:
                    self.solution.append([''.join(row) for row in self.table])
                    flag = True
                elif self.begin_position(row_index+1):
                    flag = True
                self.table[row_index][i] = '.'
            else:continue
        return flag
    
    def check_position(self,i,j):
        for k in range(i):
            if self.table[k][j] == 'Q':return False
        p,k = i-1,j-1
        while p>=0 and k>=0:
            if self.table[p][k] == 'Q':return False
            p,k = p-1,k-1
        p,k = i-1,j+1
        while p>= 0 and k<=self.n-1:
            if self.table[p][k] == 'Q':return False
            p,k = p-1,k+1
        return True

#Runtime: 132 ms
#Your runtime beats 41.19 % of python3 submissions.