class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hash_table = {}
        for a in A:
            for b in B :
                if a + b in hash_table :
                    hash_table[a+b] += 1
                else :
                    hash_table[a+b] = 1
        count = 0         
        for c in C :
            for d in D :
                if -c - d in hash_table :
                    count += hash_table[-c-d]
        return count

#Runtime: 240 ms
#Your runtime beats 81.84 % of python submissions.