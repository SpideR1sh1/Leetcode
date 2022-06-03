class Solution {
    public int divisorSubstrings(int num, int k) {
        int windowStart = 0;
        int windowNum = Integer.MAX_VALUE;
        String numb = String.valueOf(num);
        int counter = 0;
        
        for (int windowEnd = k - 1; windowEnd < numb.length(); windowEnd++) {
            String sub = numb.substring(windowStart++,windowEnd + 1);
            
            int temp = Integer.parseInt(sub);
            if (temp == 0) continue;
            else if (num %  temp == 0) {
                counter++;
            } 
            
        } return counter;
    }
}