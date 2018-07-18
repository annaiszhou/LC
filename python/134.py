class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        n, i = len(gas), 0
        while i < n:
            if gas[i] >= cost[i]: 
                res = i    
                tank = gas[i] - cost[i]
                index = res
                while tank >= 0:
                    index = (index+1) % n
                    tank += gas[index] - cost[index]
                    if index == res:
                        return res
            i += 1
        return -1

#Runtime: 1784 ms
#Your runtime beats 1.28 % of python submissions.
