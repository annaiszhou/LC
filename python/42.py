class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        max_index = height.index(max(height))
        left_index = 0
        right_index = len(height) - 1
        left_height = 0
        right_height = 0
        res = 0
        while left_index < max_index:
            if height[left_index] < left_height:
                res += left_height - height[left_index]
            else:
                left_height = height[left_index]
            left_index += 1
        while right_index > max_index:
            if height[right_index] < right_height:
                res += right_height - height[right_index]
            else:
                right_height = height[right_index]
            right_index -= 1
        return res

#Runtime: 44 ms
#Your runtime beats 99.95 % of python3 submissions.