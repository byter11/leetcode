/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {

public:
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        map<int, TreeNode*> nodeCache;
        unordered_set<int> childs;
        for(vector<int>& desc: descriptions) {
            childs.insert(desc[1]);
            int parent = desc[0];
            int child = desc[1];
            int isLeft = desc[2];
            if(nodeCache[parent] == nullptr) nodeCache[parent] = new TreeNode(parent);
            if(nodeCache[child] == nullptr) nodeCache[child] = new TreeNode(child);
            if(isLeft)
                nodeCache[parent]->left = nodeCache[child];
            else {
                nodeCache[parent]->right = nodeCache[child];
            }
        }

        for(auto node: nodeCache) {
            if(!childs.contains(node.second->val)) {
                return node.second;
            }
        }

        return nullptr;
    }
};