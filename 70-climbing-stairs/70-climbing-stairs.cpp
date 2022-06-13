class Solution {
public:
    int climbStairs(int n) {
        int cur=1, pre=0;
        for(int i=0; i<n; i++){
            cur=pre+cur;
            pre=cur-pre;
        }
        return cur;
    }
};