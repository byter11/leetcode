class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        int n = land.size();
        int m = land[0].size();

        vector<vector<int>> groups;
        int x=-1, y=-1, k = -1;

        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(land[i][j] == 1) {
                    vector<int> group = eraseGroup(land, i, j, i, j);
                    groups.push_back(group);
                }
            }
        }

        return groups;
    }

    vector<int> eraseGroup(vector<vector<int>>& land, int i, int j, int x, int y) {
        land[x][y] = 0;
        for(int k=x; k>=i; k--) land[k][y] = 0;
        for(int k=y; k>=j; k--) land[x][k] = 0; 

        if(x < land.size() - 1 && y < land[x].size() - 1 && land[x+1][y+1] == 1 && land[x+1][y] == 1 && land[x][y+1] == 1) {
            return eraseGroup(land, i, j, x+1, y+1);
        }

        if(x < land.size() - 1 && land[x+1][y] == 1) return eraseGroup(land, i, j, x+1, y);
        if(y < land[x].size() - 1 && land[x][y+1] == 1) return eraseGroup(land, i, j, x, y+1);

        return {i, j, x, y};
    }
};