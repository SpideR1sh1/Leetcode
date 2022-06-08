class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> window = new HashSet<>();
        int left = 0, right = 0;
        int longest = 0;
        int n = s.length();
        
        
        while (right < n) {
            if (window.contains(s.charAt(right))) {
                window.remove(s.charAt(left));
                left++;
            } else {
                window.add(s.charAt(right));
                right++;
            }
            longest = Math.max(longest, right - left);
            
        }
        return longest;
        
        
    }
}