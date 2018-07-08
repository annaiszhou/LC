class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res,dic,r=0,{},0
        for i,x in enumerate(s):
        	if x in dic and dic[x]>=r:
        		res=max(i-r,res)
        		r=dic[x]+1
        	dic[x]=i
        return max(res,len(s)-r)

#Runtime: 72 ms
#Your runtime beats 99.84 % of python3 submissions.