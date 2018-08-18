class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        occurences = {}
        t_set = set(t)
        counters = collections.Counter(t)
        for letter in t_set:
            if counters[letter] > s.count(letter):
                return ''
        for i in range(len(s)):
            if s[i] in t_set:
                occurences[s[i]] = occurences.get(s[i], []) + [i]
        left = len(s)
        right = 0
        for key, value in occurences.items():
            if not value:
                return ''
            for i in range(counters[key]):
                index = value.pop(0)
                left = min(left, index)
                right = max(right, index)
        min_distance = right - left
        best_left, best_right = left, right
        while left < len(s) and occurences[s[left]]:
            new_index = occurences[s[left]].pop(0)
            left += 1
            right = max(right, new_index)
            while s[left] not in t_set:
                left += 1            
            new_distance = right - left
            if new_distance < min_distance:
                best_left, best_right = left, right
                min_distance = new_distance          
        return s[best_left:best_right + 1]

#Runtime: 936 ms
#Your runtime beats 2.97 % of python submissions.