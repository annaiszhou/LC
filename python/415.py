class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        c = 0
        for i in range(min(len(num1),len(num2))):
            number = int(num1[len(num1)-i-1])+int(num2[len(num2)-i-1])+c
            c = number // 10
            res = res+(number%10)*(10**i)
        if len(num1)>=len(num2):
            num = num1
        else:
            num = num2
        length = len(num)
        for j in range(i+1,length):
            number = int(num[length-j-1])+c
            c = number // 10
            res = res+(number%10)*10**j
        if c == 0:
            return str(res)
        else:
            return str(res+c*10**(length))

#Runtime: 384 ms
#Your runtime beats 7.12 % of python submissions.

'''
        carry = 0
        l1 = len(num1) - 1
        l2 = len(num2) - 1
        res = ''
        while(l1 >= 0 or l2 >= 0 or carry > 0):
            if l1 >= 0:
                carry += int(num1[l1]); l1-=1
            if l2 >=0 :
                carry += int(num2[l2]); l2-= 1
            res = str(carry % 10) + res
            carry = carry // 10
        return res
'''