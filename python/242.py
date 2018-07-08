class Solution:
	def isAnagram(self, s, t):
	    """
	    :type s: str
	    :type t: str
	    :rtype: bool
	    """
	    if len(s)==0:
	    	return True
	    if len(s)!=len(t):
	    	return False
	    dic={}
	    for i in s:
	    	if i not in dic:
	    		dic[i]=1
	    	else:
	    		dic[i]=dic[i]+1
	    for j in t:
	    	if j not in dic:
	    		return False
	    	dic[j]=dic[j]-1
	    	if dic[j] < 0:
	    		return False 
	    return True

#Runtime: 52 ms
#Your runtime beats 82.19 % of python3 submissions.