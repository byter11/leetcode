class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();

        int islands = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(grid[i][j] == '1') {
                    islands++;
                    eraseIsland(grid, i, j);
                }
            }
        }

        return islands;
    }

    void eraseIsland(vector<vector<char>>& grid, int i, int j) {
        if(i < 0 || i >= grid.size() || j < 0 || j >= grid[i].size()) return;
        if(grid[i][j] == '0') return;

        grid[i][j] = '0';
        eraseIsland(grid, i+1, j);
        eraseIsland(grid, i-1, j);
        eraseIsland(grid, i, j+1);
        eraseIsland(grid, i, j-1);
    }
};