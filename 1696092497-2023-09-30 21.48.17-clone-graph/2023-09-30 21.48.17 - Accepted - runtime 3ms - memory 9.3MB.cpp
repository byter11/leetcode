/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
    vector<Node *> cache;
public:
    Node* cloneGraph(Node* node) {
        if(!node) return nullptr;
        
        Node* g = new Node();
        cache = vector<Node *>(101, nullptr);
        cloneDFS(node, g);
        return g;
    }

    void cloneDFS(Node* in, Node* out) {
        if(!in || !out) return;
        out->val = in->val;
        cache[out->val] = out;
        for(Node* n : in->neighbors) {
            if(cache[n->val] != nullptr) {
                out->neighbors.push_back(cache[n->val]);
            } else {
                Node* newNode = new Node();
                out->neighbors.push_back(newNode);
                cloneDFS(n, newNode);
            }
        }
    }
};