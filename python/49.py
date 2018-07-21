class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str in strs:
            s = ''.join(sorted(str))
            if s in dic:
                dic[s].append(str)
            else:
                dic[s] = [str]
        res = [dic[x] for x in dic]
        return res

#Runtime: 124 ms
#Your runtime beats 89.24 % of python submissions.
            