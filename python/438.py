class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        dic_p, dic_s = {}, {}
        len_p, len_s = len(p), len(s)
        if len_s < len_p:
            return []
        for char in p:
            dic_p[char] = dic_p.get(char, 0) + 1
        char_list = dic_p.keys() 
        for char in char_list:
            dic_s[char] = 0 
        for i in range(len_p):
            if s[i] in char_list:
                dic_s[s[i]] += 1
        if dic_s == dic_p:
            res.append(0)
        for i in range(len_p, len_s):
            if s[i] in char_list:# adding the new element
                dic_s[s[i]] += 1
            if s[i - len_p] in char_list:# removing the oldest element
                dic_s[s[i - len_p]] -= 1
            if dic_s == dic_p: # Checking to see if we have anagram
                res.append(i - len_p + 1)
        return(res)

#Runtime: 116 ms
#Your runtime beats 97.41 % of python submissions.