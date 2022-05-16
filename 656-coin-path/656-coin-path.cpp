class Solution {
public:
     vector<int> cheapestJump(vector<int>& A, int B) {
        vector<int> dp(A.size(), -1), res(1, 1);
        dp.back()=0;
        for(int i=A.size()-1;i>=0;i--) {
            if(A[i]==-1) continue;
            for(int j=i+1;j<A.size()&&j<=i+B;j++) {
                if(A[j]==-1||dp[j]==-1) continue;
                if(dp[i]==-1) dp[i]=dp[j];
                else dp[i]=min(dp[i], dp[j]);
            }
            if(dp[i]!=-1) dp[i]+=A[i];
        }
        if(dp[0]==-1) return {};
        int i=0, cost=dp[0];
        while(i<A.size()-1) {
            for(int j=i+1;j<A.size()&&j<=i+B;j++) {
                if(dp[j]==cost-A[i]) { 
                    res.push_back(j+1);
                    cost-=A[i];
                    i=j;
                    break;
                }
            }
        }
        return res;
    }
};