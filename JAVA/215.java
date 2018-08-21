class Solution {
    public int findKthLargest(int[] nums, int k) {
        int temp;
        for (int i = 0 ; i < nums.length-1 ; i ++){
            for (int j = 0 ; j < nums.length-i-1 ; j ++){
                if (nums[j+1] < nums[j]){
                    temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp;
                }
            }
        }
        return nums[nums.length-k];
    }
}

#Runtime: 232 ms
#beat 0%
#Bubble Sort
#O(n^2)