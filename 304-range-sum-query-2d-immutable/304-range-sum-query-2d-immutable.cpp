class NumMatrix {
public:
    vector<vector<int>> dp;
    NumMatrix(vector<vector<int>> &mat) {
        dp.resize(mat.size()+1, vector<int>(mat[0].size()+1));
        for(int i=1;i<=mat.size();i++) 
            for(int j=1;j<=mat[0].size();j++) 
            dp[i][j] = mat[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1];
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return dp[row2+1][col2+1] - dp[row2+1][col1] - dp[row1][col2+1] + dp[row1][col1];
    }
};