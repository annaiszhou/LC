class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        res = [[0] * n for _ in xrange(m)]
        self.dfs(dungeon, 0, 0, res)
        return res[0][0]

    def dfs(self, M, i, j, res):
        m, n = len(M), len(M[0])   
        if i >= m or j >= n:
            return float('inf')

        if res[i][j] != 0:
            return res[i][j]

        health = float('inf')
        down = self.dfs(M, i+1, j, res)
        right = self.dfs(M, i, j+1, res)
        health = min(health, down, right)

        if health == float('inf'):
            health = 1 - M[i][j] if M[i][j] < 0 else 1
        elif health > M[i][j]:
            health = health - M[i][j]
        else:
            health = 1

        res[i][j] = health
        return res[i][j]

#Runtime: 48 ms
#Your runtime beats 18.04 % of python submissions.