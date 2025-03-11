class Solution {
    vector<vector<int>> vis;
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int n = heights.size(), m = heights[0].size();
        vis = vector<vector<int>>(n);
        vector<vector<int>> res;

        for(int i=0; i<n; i++) {
            vis[i] = vector<int>(m, 0);
        }



        // for(int i=0; i<n; i++) {
        //     for(int j=0; j<m; j++) {
        //         cout << heights[i][j] << ' ';
        //     }
        //     cout << '\n';
        // }
    
        for(int i=0; i<n; i++) {
            dfs(heights, i, 0, -1, 1);
        }
        for(int j=0; j<m; j++) {
            dfs(heights, 0, j, -1, 1);
        }
        for(int i=0; i<n; i++) {
            dfs(heights, i, m-1, -1, 2);
        }
        for(int j=0; j<m; j++) {
            dfs(heights, n-1, j, -1, 2);
        }

        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(vis[i][j] == 3) res.push_back({i,j});
                // cout << vis[i][j] << ' ';
            }
            // cout << '\n';
        }

        return res;
    }

    void bfs(vector<vector<int>>& h, int i, int j, int mark, int dir) {
        queue<vector<int>> q;
        q.push({i, j, mark});

        while(!q.empty()) {
            vector<int> t = q.front(); q.pop();
            int i = t[0], j = t[1], f = t[2];
            cout << i << ' ' << j << " | ";
            vis[i][j] |= f;

            if(i < h.size() && j+dir < h[0].size() && i >= 0 && j+dir >= 0) {
                int j_mark = h[i][j] < h[i][j+dir] ? f : 0;
                q.push({i, j+dir, j_mark});
            }
            if(i+dir < h.size() && j < h[0].size() && i+dir >= 0 && j >= 0) {
                int i_mark = h[i][j] < h[i+dir][j] ? f : 0;
                q.push({i+dir, j, i_mark});
            }
        }
    }

    void dfs(vector<vector<int>>& h, int i, int j, int p, int m) {
        if(i < 0 || j < 0)
            return; 
        if(i >= h.size() || j >= h[0].size())
            return;
        if(h[i][j] < p) return;
        if(vis[i][j] & m) return;

        vis[i][j] |= m;

        dfs(h, i+1, j, h[i][j], m);
        dfs(h, i-1, j, h[i][j], m);
        dfs(h, i, j+1, h[i][j], m);
        dfs(h, i, j-1, h[i][j], m);
    }
};

