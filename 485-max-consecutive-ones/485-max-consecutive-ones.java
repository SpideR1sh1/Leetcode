class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int left = 0, right = 0, sum = Integer.MIN_VALUE;
        int n = nums.length;
        
        
        for (right = 0; right < n; right++) {
            
            
            if (nums[right] == 0) {
                sum = Math.max(sum, right - left);
                left = right + 1;
            } else {
                sum = Math.max(sum, right - left + 1);
            }
            

        }
        
        return sum;
    }
}