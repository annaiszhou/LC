class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        height = {k:0 for k in range(n)}
        graph = {k:set([]) for k in range(n)}
        for edge in edges:
            u,v = edge[0], edge[1]
            height[u], height[v] = height[u]+1, height[v]+1
            graph[u].add(v)
            graph[v].add(u)
        leaves = [k for k,v in height.items() if v == 1]
        while leaves and len(graph) > 2:
            for leaf in leaves:
                v = graph[leaf].pop()
                del graph[leaf]
                del height[leaf]
                height[v] -= 1
                graph[v].remove(leaf)
            leaves = [k for k,v in height.items() if v == 1]
        return list(graph.keys())

#Runtime: 476 ms
#Your runtime beats 18.74 % of python submissions.