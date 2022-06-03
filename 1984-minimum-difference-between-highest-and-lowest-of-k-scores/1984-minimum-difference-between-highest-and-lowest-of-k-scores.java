class Solution {
    public int minimumDifference(int[] nums, int k) {
        Arrays.sort(nums);
        int windowDiff = Integer.MAX_VALUE;
        
        for (int i = 0; i < nums.length; i++) {
            if (i + k - 1 >= nums.length) break;
            windowDiff = Math.min(windowDiff, nums[i + k - 1] - nums[i]);
        }
        return windowDiff;
        
        
        
    }
}