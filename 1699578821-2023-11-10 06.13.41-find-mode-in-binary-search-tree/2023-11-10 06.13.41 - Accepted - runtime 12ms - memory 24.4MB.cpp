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
    int mode = 0;
    int consec = 0;
    TreeNode* prev;
    vector<int> modes;

public:
    vector<int> findMode(TreeNode* root) {
        setMode(root, false);
        cout << mode << '\n';

        consec = 1;
        prev = NULL;
        modes = vector<int>();
        setMode(root, true);
        return modes;
    }

    void setMode(TreeNode* root, bool setList) {
        if(mode < consec) mode = consec;
        if(!root) return;

        
        setMode(root->left, setList);
        consec = prev && root->val == prev->val ? consec+1 : 1;
        if(consec == mode) modes.push_back(root->val);
        prev = root;
        setMode(root->right, setList);
    }
};