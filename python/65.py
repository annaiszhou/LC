class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        
        def isNumber(s):
        	if s == "":
        		return False
        	for ss in s:
        		if not '0'<=ss<='9':
        			return False
        	return True
        
        def isPositive(s):
            return (s != "" and s[0] == '+' and isNumber(s[1:])) or isNumber(s)
        
        def isNegtive(s):
            return (s != "" and s[0] == '-' and isNumber(s[1:])) or isNumber(s)
        
        def isInteger(s):
            return isPositive(s) or isNegtive(s)
        
        def isFloat(s):
            float_point = s.find('.')
            if float_point != -1:
                if isInteger(s[:float_point]):
                    return s[float_point + 1:] == "" or isNumber(s[float_point + 1:])
                elif s[:float_point] == "" or s[:float_point] == "+" or s[:float_point] == "-":
                    return isNumber(s[float_point + 1:])
                else:
                    return False
            else:
                return isInteger(s)

        e = s.find('e')
        if e != -1:
        	return isFloat(s[:e]) and isInteger(s[e + 1:])
        else:
        	return isFloat(s)

#Runtime: 40 ms
#Your runtime beats 25.79 % of python submissions.