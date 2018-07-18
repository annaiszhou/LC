class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        integer_string1 = []
        integer_string2 = []
        for i in range(len(num1)):
            integer_string1.append(ord(num1[i])-ord('0'))
        integer1 = 0
        for j in range(len(integer_string1)):
            integer1 = integer1*10 + integer_string1[j]
        for i in range(len(num2)):
            integer_string2.append(ord(num2[i])-ord('0'))
        integer2 = 0
        for j in range(len(integer_string2)):
            integer2 = integer2*10 + integer_string2[j]
        multiply = integer1 * integer2
        res_list =[]
        res = ''
        if(multiply==0):
            return '0'
        while(multiply>0):
            n = multiply%10
            multiply = int(multiply/10)
            res_list.append(chr(n+ord('0')))
        for i in range(len(res_list)-1,-1,-1):
            res += (res_list[i])
        return res

#Runtime: 32 ms
#Your runtime beats 88.98 % of python submissions.