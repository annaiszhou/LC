class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        res = 0
        i = 0
        for house in houses:
            while i < len(heaters) and heaters[i] < house:
                i += 1
            if i == 0:
                res = max(res, heaters[i] - house)
            elif i == len(heaters):
                return max(res, houses[-1] - heaters[-1])
            else:
                res = max(res, min(heaters[i]-house, house-heaters[i-1]))
        return res

#Runtime: 68 ms
#Your runtime beats 97.28 % of python submissions.