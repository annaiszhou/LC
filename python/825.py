from collections import Counter
class Solution(object):
    '''
    #O(n^2)
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        res=0
        for i in range(len(ages)):
            for j in range(i+1,len(ages)):
                print i,j
                if ages[i]<=0.5*ages[j]+7 or ages[i]>ages[j] or (ages[i]>100 and ages[j]<100):
                    None
                else:
                    print ages[i],ages[j]
                    res+=1
                if ages[j]<=0.5*ages[i]+7 or ages[j]>ages[i] or (ages[j]>100 and ages[i]<100):
                    None
                else:
                    print ages[i],ages[j]
                    res+=1
        return res
    '''
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        new_age = [age for age in ages if age>14]
        count_age = Counter(new_age)
        res = 0
        for i in count_age:
            for j in count_age:
                print i,j
                if i<j:
                    if i<=0.5*j+7 or i>j or i>100 and j<100:
                        None
                    else:
                        print 1
                        res+=count_age[i]*count_age[j]
                    if j<=0.5*i+7 or j>i or j>100 and i<100:
                        None
                    else:
                        print 1
                        res+=count_age[i]*count_age[j]
                else:
                    continue
        return res
    
if __name__ == '__main__':
    ages=[16,16]
    print(Solution().numFriendRequests(ages))

#Runtime: 148 ms
#Your runtime beats 39.29 % of python submissions.
