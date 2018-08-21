class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def helper(v, color):
            if v in colored:
                return True if colored[v] == color else False 
            else:
                colored[v] = color
                for u in graph[v]:
                    if not helper(u, (color+1)%2):
                        return False
                return True
        
        colored = {} 
        for v in range(len(graph)):
            if v not in colored:
                if helper(v, 0) is False:
                    return False
        return True

#Runtime: 60 ms
#Your runtime beats 35.62 % of python3 submissions.
