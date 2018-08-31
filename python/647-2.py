class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        mark = [0 for i in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            res+=1
            mark[i]=1
            for j in range(len(s)-1,i,-1):
                if s[i]==s[j] and mark[j-1]==1:
                    res+=1
                    mark[j]=1
                else:
                    mark[j]=0
        return res

#Runtime: 136 ms
#Your runtime beats 53.51 % of python submissions.