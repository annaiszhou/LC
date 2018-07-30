class Solution(object):
    def findMinStep(self, board, hand):
    
        self.res = float("inf")
        self.length = len(hand)
        count = collections.Counter(hand)
    
        def helper(board, n, count):
            if not board:
                self.res = min(self.res, self.length - n)
                return 
            for i, char in enumerate(board):
                if i > 0 and char == board[i - 1]:
                    continue
                j = i
                while j < len(board) and board[j] == char:
                    j += 1
                if j - i >= 3:
                    helper(board[:i] + board[j:], n, count)
                elif j - i == 2 and count[char] > 0:
                    count[char] -= 1
                    helper(board[:i] + board[j:], n - 1, count)
                    count[char] += 1
                elif count[char] > 0:
                    count[char] -= 1
                    helper(board[:i] + char + board[i:], n - 1, count)
                    count[char] += 1
            
        helper(board, len(hand), count)
        if self.res != float("inf"):
            return self.res
        else:
            return -1

#Runtime: 480 ms
#Your runtime beats 13.64 % of python submissions.