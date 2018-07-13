class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        word_set = set(wordList)
        head = []
        head.append(beginWord)
        tail = []
        tail.append(endWord)
        word_set.discard(beginWord)
        word_set.discard(endWord)
        alphabets = [chr(ord('a')+i) for i in range(26)]
        graph = collections.defaultdict(list)

        terminate = False
        left_to_right = True
        while head:
            new_words = set()
            for i in range(len(head)):
                cur_word = head.pop()
                for j in range(len(cur_word)):
                    for alpha in alphabets:
                        new_word = cur_word[:j] + alpha + cur_word[j+1:]
                        if new_word in tail:
                            terminate = True
                        if new_word in tail or new_word in word_set:
                            if left_to_right:
                                graph[cur_word].append(new_word)
                            else:
                                graph[new_word].append(cur_word)
                        if new_word in word_set:
                            new_words.add(new_word)
            if terminate:
                break            
            head = new_words
            for new_word in new_words:
                word_set.discard(new_word)
                
            if len(head) > len(tail):
                head, tail = tail, head
                left_to_right = not left_to_right

        def helper(graph, word, target, result, results):
            if word == target:
                results.append(result[:])
            for w in graph[word]:
                result.append(w)
                helper(graph, w, target, result, results)
                result.pop()
            return
        
        results = []
        helper(graph, beginWord, endWord, [beginWord], results)            
        return results

#Runtime: 108 ms
#Your runtime beats 96.03 % of python3 submissions.