class Solution:             
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range((len(num) - 1) // 2):
            if num[0] == "0" and i > 0:
                break
            for j in range(i + 1, min((len(num) - i - 1) // 2 + i + 1, len(num) - i - 1)):
                if num[i + 1] == "0" and j > i + 1:
                    break
                if self.helper(num, i, j):
                    return True
        return False

    def helper(self, num, i1, i2):
        n1 = num[: i1 + 1]
        n2 = num[i1 + 1: i2 + 1]
        n1, n2 = n2, str(int(n1) + int(n2))
        i = i2 + 1
        while True:
            i2 = 0
            while i2 < len(n2) and i < len(num) and n2[i2] == num[i]:
                i2 += 1
                i += 1                    
            if i2 == len(n2):
                if i == len(num):
                    return True
                else:
                    n1, n2 = n2, str(int(n1) + int(n2))
            else:
                return False       

#Runtime: 20 ms
#Your runtime beats 100.00 % of python submissions.