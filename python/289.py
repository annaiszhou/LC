class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def cheak(i,j):
            res=0
            for a,b in [(i-1,j),(i-1,j-1),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]:
                try:
                    if a>-1 and b>-1 and board[a][b]%2:
                        res+=1
                except:
                    pass
            return res
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                g=cheak(i,j)
                if board[i][j]%2==1 and (g==2 or g==3):
                    board[i][j]+=2
                    continue
                if board[i][j]%2==0 and g==3:
                    board[i][j]+=2

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]//=2       

#Runtime: 24 ms
#Your runtime beats 68.07 % of python submissions.