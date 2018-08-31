class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(check):
        	return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        res = []
        for word, k in words.iteritems():
        	n = len(word)
        	for j in range(n+1):
        		pref = word[:j]
        		suf = word[j:]
        		if is_palindrome(pref):
        			back = suf[::-1]
        			if back != word and back in words:
        				res.append([words[back],  k])
        		if j != n and is_palindrome(suf):
        			back = pref[::-1]
        			if back != word and back in words:
        				res.append([k, words[back]])
        return res