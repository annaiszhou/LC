class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1,len(s)):
        	if len(s)%i == 0:
        		if s[0:i]*(len(s)//i) == s:
        			return True
        		else:
        			continue
        return False

#Runtime: 56 ms
#Your runtime beats 50.25 % of python submissions.
