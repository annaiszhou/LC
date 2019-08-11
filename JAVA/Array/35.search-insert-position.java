/*
 * @lc app=leetcode id=35 lang=java
 *
 * [35] Search Insert Position
 */
class Solution {
    public int searchInsert(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                return i;
            }
            if (nums[i] > target) {
                return i;
            }
        }
        return nums.length;
    }
}

