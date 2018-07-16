class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_people = sorted(sorted(people,key=lambda x:x[1],reverse=True),key=lambda y:y[0])
        res = []
        for everyone in reversed(sorted_people):
            res.insert(everyone[1],everyone)
        return res

#Runtime: 80 ms
#Your runtime beats 97.67 % of python submissions.