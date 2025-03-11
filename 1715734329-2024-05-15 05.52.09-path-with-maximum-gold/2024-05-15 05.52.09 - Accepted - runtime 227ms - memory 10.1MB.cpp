class Solution {
public:
    int getMaximumGold(vector<vector<int>>& grid) {
        int ans = 0;
        for(int i=0; i<grid.size(); i++) {
            for(int j=0; j<grid[i].size(); j++) {
                ans = max(ans, maxGold(grid, i, j));
            }
        }

        return ans;
    }

    int maxGold(vector<vector<int>>& grid, int i, int j) {
        if(i < 0 || j < 0 || i >= grid.size() || j >= grid[i].size() || grid[i][j] == 0) return 0;
        
        int val = grid[i][j];
        grid[i][j] = 0;

        int maxVal = val + max({
            maxGold(grid, i+1, j),
            maxGold(grid, i, j+1),
            maxGold(grid, i-1, j),
            maxGold(grid, i, j-1)
        });

        grid[i][j] = val;

        return maxVal;
    }
};