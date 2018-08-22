class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """        
        if start == end:
            return 0
        queue = collections.deque()
        queue.append(start)
        visited = set()
        visited.add(start)
        res = 0
        while queue:
        	new_queue = collections.deque()
        	gene = queue.pop()
        	for mutation in bank:
        		if mutation not in visited and self.helper(gene,mutation):
        			if mutation == end:
        				res+=1
        				return res
        			new_queue.append(mutation)
        			visited.add(mutation)
        	queue = new_queue
        	res+=1
        return -1

    def helper(self,gene,mutation):
        one = 0
        for i in range(len(gene)):
        	if gene[i] != mutation[i]:
        		one+=1
        return True if one ==1 else False

#Runtime: 20 ms
#Your runtime beats 99.46 % of python submissions.