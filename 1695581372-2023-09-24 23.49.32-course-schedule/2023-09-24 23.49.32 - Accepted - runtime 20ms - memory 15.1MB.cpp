class Solution {
    unordered_map<int, vector<int>> g;
    vector<int> vis;
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vis = vector<int>(numCourses, -1);
        for(auto &p: prerequisites) {
            g[p[0]].push_back(p[1]);
        }
    
        for(int i=0; i<numCourses; i++) {
            if(g.contains(i)) {
                if(!can_take(i))
                    return false;
            }
        }
        return true;
    }

    bool can_take(int i) {
        if(vis[i] != -1) return vis[i];
        if(g[i].empty()) {
            vis[i] = 1;
            return true;
        }

        vis[i] = 0;
        for(int &j: g[i]) {
            if(!can_take(j)) return false;
        }

        cout << "can take " << i << " now.\n";
        vis[i] = 1;
        return true;
    }
};