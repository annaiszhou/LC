class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = []
        if len(a) > len(b):
            l = a
        else:
            l = b
        a = list(reversed(a))
        b = list(reversed(b))
        for i in range(len(l)):
            if i + 1 > len(a):
                n = int(b[i])
                t = 0
            elif i + 1 > len(b):
                n = int(a[i])
                t = 0 
            else: 
                n = int(a[i])
                t = int(b[i])            
            if n + t + carry == 2:
                carry = 1
                result.append('0')
            elif n + t + carry == 3:
                carry = 1 
                result.append('1')
            else:                
                result.append(str(n + t + carry))
                carry = 0 
        if carry == 1:
            result.append(str(carry))        
        result = reversed(result)
        return "".join(result)

#Runtime: 32 ms
#Your runtime beats 56.08 % of python submissions.