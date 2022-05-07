class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int n = nums.size();
        int start = 0, end = -1;
        
        int min_ = INT_MAX;
        for (int i = 0; i < n; i++) 
            if (nums[n-i-1] <= min_) min_ = nums[n-i-1];
            else  start = n-i-1;

        int max_ = INT_MIN;
        for (int i = 0 ; i < n; i++)
            if (nums[i] >= max_) max_ = nums[i];
            else end = i;
    
        return end - start + 1;
    }
};