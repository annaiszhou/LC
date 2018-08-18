class Solution(object):
	def floodFill(self, image, sr, sc, newColor):
	    """
	    :type image: List[List[int]]
	    :type sr: int
	    :type sc: int
	    :type newColor: int
	    :rtype: List[List[int]]
	    """
	    oldColor = image[sr][sc]        
	    row, col = len(image), len(image[0])     
	    if oldColor == newColor:
	        return image
	    stack = [(sr, sc)]  
	    memory = set((sr, sc))
	    while stack:
	        r, c = stack.pop()
	        image[r][c] = newColor
	        for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
	            new_r, new_c = r + i, c + j
	            if (new_r, new_c) not in memory and 0 <= new_r < row and 0 <= new_c < col and image[new_r][new_c] == oldColor:
	                stack.append((new_r, new_c))
	                memory.add((new_r, new_c))
	    return image

#Runtime: 56 ms
#Your runtime beats 87.88 % of python submissions.