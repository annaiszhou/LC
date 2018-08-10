class Solution(object):
    def __init__(self):
        self.g = {}
        
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            if a not in self.g:
                self.g[a] = set()
            self.g[a].add((b, val))
            if b not in self.g:
                self.g[b] = set()
            self.g[b].add((a, 1 / val))
        res = []
        for q in queries:
            fr, to = q
            if fr not in self.g:
                res.append(-1.0)
            elif to not in self.g:
                res.append(-1.0)
            elif fr == to:
                res.append(1.0)
            else:
                visited = set()
                queue = [(fr, 1)]
                isFound = False
                while queue:
                    level = []
                    count = len(queue)
                    for i in range(count):
                        node, val = queue.pop(0)
                        if node == to:
                            res.append(val)
                            isFound = True
                            break
                        visited.add(node)
                        for neighbor, v2 in self.g[node]:
                            if neighbor not in visited:
                                level.append((neighbor, val * v2))
                    queue = level
                if not isFound:
                    res.append(-1.0)
        return res

#Runtime: 20 ms
#Your runtime beats 100.00 % of python submissions.