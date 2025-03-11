class Solution {
    vector<vector<int>> memo;
public:
    int countNegatives(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        memo = vector<vector<int>>(n+1);
        for(int i=0; i<n; i++) memo[i] = vector<int>(m+1, 0);

        return dfs(grid, n-1, m-1);
    }

    int dfs(vector<vector<int>>& grid, int i, int j) {
        if(i < 0 || j < 0 || grid[i][j] >= 0 || memo[i][j] == 1) return 0;
        memo[i][j] = 1;

        return 1 + dfs(grid, i-1, j) + dfs(grid, i, j-1);
    }
};


// 4 3 2 -1
// 3 2 1 -1
// 1 1 -1 -2
// -1 -1 -2 -3