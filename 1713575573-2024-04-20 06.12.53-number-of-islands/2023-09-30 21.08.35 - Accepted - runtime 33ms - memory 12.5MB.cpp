class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int ans = 0;
        for(int i=0; i<grid.size(); i++) {
            for(int j=0; j<grid[i].size(); j++) {
                if(grid[i][j] == '1') {
                    ans++;
                    eraseIsland(grid, i, j);
                }
            }
        }

        return ans;
    }

    void eraseIsland(vector<vector<char>>& grid, int i , int j) {
        if(i < 0 || j < 0 || i >= grid.size() || j >= grid[i].size() || grid[i][j] == '0') return;

        grid[i][j] = '0';
        eraseIsland(grid, i+1, j);
        eraseIsland(grid, i, j+1);
        eraseIsland(grid, i-1, j);
        eraseIsland(grid, i, j-1);
    }
};