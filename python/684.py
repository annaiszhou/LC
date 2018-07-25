class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        connected_edge = set()
        removed_edge = []
        for edge in edges:
            start=end=None
            for s in connected_edge:
                if start and end:
                    break
                if edge[0] in s:
                    start = s
                if edge[1] in s:
                    end = s
            if start and end:
                if start == end:
                    removed_edge.append(edge)
                else:
                    merged = set(start) | set(end)
                    connected_edge.discard(start)
                    connected_edge.discard(end)
                    connected_edge.add(frozenset(merged))
            elif not start and not end:
                connected_edge.add(frozenset(edge))
            elif start and not end:
                merged = set(start) | set(edge)
                connected_edge.discard(start)
                connected_edge.add(frozenset(merged))
            elif not start and end:
                merged = set(end) | set(edge)
                connected_edge.discard(end)
                connected_edge.add(frozenset(merged))
        return removed_edge[-1]

#Runtime: 160 ms
#Your runtime beats 1.36 % of python submissions.