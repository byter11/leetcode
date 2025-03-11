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
    unordered_set<TreeNode*> roots;
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        roots = unordered_set<TreeNode*>();
        roots.insert(root);
        unordered_set<int> toDelete;
        for(int &i: to_delete) toDelete.insert(i);

        findAndDelNodes(root, nullptr, false, toDelete);

        vector<TreeNode*> ans;
        for(auto n: roots) ans.push_back(n);
        return ans;
    }

    void findAndDelNodes(TreeNode* root, TreeNode *parent, bool isLeft, unordered_set<int>& toDelete) {
        if(!root) return;
        if(toDelete.contains(root->val)) {
            if(parent != nullptr) {
                if(isLeft) parent->left = nullptr;
                else parent->right = nullptr;
            }
            roots.erase(root);
            if(root->left != nullptr) roots.insert(root->left);
            if(root->right != nullptr) roots.insert(root->right);
        }

        findAndDelNodes(root->left, root, true, toDelete);
        findAndDelNodes(root->right, root, false, toDelete);
    }
};