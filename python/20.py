class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        value = {'(':')','[':']','{':'}',')':')',']':']','}':'}'}
        if not s:
        	return True
        stack = [s[0]]
        i = 1
        while i<len(s):
            if not stack:
                stack.append(s[i])
                i += 1
            else:
                temp = stack[-1]
                if value[temp] == s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
                i += 1
        print stack
        if not stack:
        	return True
        else:
        	return False

#Runtime: 36 ms
#Your runtime beats 15.32 % of python submissions.



