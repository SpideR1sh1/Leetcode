class Solution {
    public int dietPlanPerformance(int[] calories, int k, int lower, int upper) {
        int windowStart = 0;
        int windowSum = 0;
        int points = 0;
        for (int windowEnd = 0; windowEnd < calories.length; windowEnd++) {
            windowSum += calories[windowEnd];
            
            if (windowEnd >= k-1) {
                if (windowSum > upper) {
                    points++;
                } else if (windowSum < lower) {
                    points--;
                }
                windowSum -= calories[windowStart];
                windowStart++;
                
            }
        }
        return points;
    }
}