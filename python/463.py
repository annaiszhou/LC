class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        for x in range (len(grid)):
            for y in range (len(grid[0])):
                if grid[x][y] == 1: 
                    for direction in directions: 
                        checkx = x + direction[0] 
                        checky = y + direction[1]
                        if checkx > -1 and checky > -1 and checkx < len(grid) and checky < len(grid[0]): 
                            if grid[checkx][checky] == 0:
                                res += 1
                        else: 
                            res += 1    
                else:
                    continue
        return res

#Runtime: 392 ms
#Your runtime beats 32.61 % of python3 submissions.