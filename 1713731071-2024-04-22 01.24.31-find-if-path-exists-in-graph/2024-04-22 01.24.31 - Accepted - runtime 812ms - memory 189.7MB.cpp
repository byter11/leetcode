class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        if(source == destination) return true;

        map<int, vector<int>> graph;
        for(auto &edge: edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        if(!graph.contains(source) || !graph.contains(destination)) return false;

        queue<int> q;
        unordered_set<int> visited;
        q.push(source);

        while(!q.empty()) {
            source = q.front(); q.pop();
            visited.insert(source);
            if(source == destination) return true;

            for(int node: graph[source]) {
                if(!visited.contains(node))
                    q.push(node);
            }
        }

        return false;
    }
};