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
    int averageOfSubtree(TreeNode* root) {
        int ans = 0;
        calc_avgn(root, ans);
        return ans;
    }

    pair<int,int> calc_avgn(TreeNode* root, int &ans) {
        if(!root->left && !root->right) {
            ans++;
            return {1, root->val};
        };

        pair<int,int> sum = {1, root->val};
        if(root->left) {
            pair<int,int> left = calc_avgn(root->left, ans);
            sum.first += left.first;
            sum.second += left.second;

        }
        if(root->right){
            pair<int,int> right = calc_avgn(root->right, ans);
            sum.first += right.first;
            sum.second += right.second;
        };

        if (sum.second/sum.first == root->val) {
            ans++;
        }

        return {sum.first, sum.second};
    }
};

