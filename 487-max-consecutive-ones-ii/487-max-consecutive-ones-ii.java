class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int windowStart = 0, windowSum = 0, windowEnd = 0;
        int numZeroes = 0;
        
        while (windowEnd < nums.length) {
            if (nums[windowEnd] == 0) {
                numZeroes++;
            }
            
            while (numZeroes == 2) {
                if (nums[windowStart] == 0) {
                    numZeroes--;
                }
                windowStart++;
            }
            
            windowSum = Math.max(windowSum, windowEnd - windowStart + 1);
            windowEnd++;
        }
        return windowSum;
    }
}