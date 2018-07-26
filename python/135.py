class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        j,num,res = 1,1,0
        for i in range(len(ratings)):
            if i==0 or ratings[i-1]==ratings[i]:
                num = 1
            elif ratings[i-1]>ratings[i]:
                num = num-1
            else:
                num = num+1
            res += num
            if i==0 or ratings[i]>=ratings[i-1]:
                j = i
            if i==len(ratings)-1 or ratings[i+1]>=ratings[i]:
                if num > 1:
                    res += (i-j)*(1-num)
                if num < 1:
                    res += (i-j+1)*(1-num)
                if not i==j:
                    num = 1
        return res

#Runtime: 52 ms
#Your runtime beats 59.72 % of python submissions.