class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>> ans(n-2);
        for(int i=0; i<n-2; i++) {
            ans[i] = vector<int>(m-2, 0);
        }

        for(int i=1; i<n-1; i++) {
            for(int j=1; j<m-1; j++) {
                ans[i-1][j-1] = max({
                    grid[i-1][j-1],
                    grid[i-1][j],
                    grid[i-1][j+1],
                    grid[i][j-1],
                    grid[i][j],
                    grid[i][j+1],
                    grid[i+1][j-1],
                    grid[i+1][j],
                    grid[i+1][j+1]
                });
            }
        }

        return ans;
    }
};