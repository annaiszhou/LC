class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
        	return True
        string = ''.join(c for c in s if c.isalnum()).lower()
        i = 0
        j = len(string)-1
        while i<j:
        	if string[i] != string[j]:
        		return False
        	i+=1
        	j-=1
        return True

#Runtime: 40 ms
#Your runtime beats 85.43 % of python submissions.