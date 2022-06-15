class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int windowStart = 0, maxLen = Integer.MIN_VALUE;
        
        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            char right = s.charAt(windowEnd);
            map.put(right, map.getOrDefault(right, 0) + 1);
            
            while (map.size() > 2) {
                char left = s.charAt(windowStart);
                map.put(left, map.get(left) - 1);
                
                if (map.get(left) == 0) {
                    map.remove(left);
                }
                windowStart++;
            }
            maxLen = Math.max(maxLen, windowEnd - windowStart + 1);
            
        }
        return maxLen;
        
        
        
    }
}