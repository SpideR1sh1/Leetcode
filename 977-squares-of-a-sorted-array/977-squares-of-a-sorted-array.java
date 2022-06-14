class Solution {
    public int[] sortedSquares(int[] nums) {
        int left = 0;
        for (left = 0; left < nums.length; left++) {
            nums[left] = nums[left] * nums[left];
        }
        Arrays.sort(nums);
        return nums;
    }
}