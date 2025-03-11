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
    bool findTarget(TreeNode* root, int k) {
        unordered_set<int> s;
        build_set(root, s);
        
        for(int val : s) {
            if(k-val != val && s.find(k-val) != s.end()) 
                return true;
        }
        return false;
    }
    
    void build_set(TreeNode* root, unordered_set<int>& s) {
        if(!root) return;
        s.insert(root->val);
        build_set(root->left, s);
        build_set(root->right, s);
    }
};