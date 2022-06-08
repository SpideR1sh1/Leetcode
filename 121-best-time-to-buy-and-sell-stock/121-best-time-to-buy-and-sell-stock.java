class Solution {
    public int maxProfit(int[] prices) {
        int buy = Integer.MAX_VALUE;
        int maxProfit = Integer.MIN_VALUE;
        int sell = 0;
        for (int price : prices) {
            
            if (price < buy) {
                buy = price;
            } else {
                sell = Math.max(sell, price - buy);
            }
            
            
        }
        return sell;
    }
}