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
    string getDirections(TreeNode* root, int startValue, int destValue) {   
        string path = "";
        string startPath = getPath(root, startValue, path);
        string destPath = getPath(root, destValue, path);

        int i=0;
        while(i < startPath.size() && i < destPath.size() && startPath[i] == destPath[i]) i++;

        path = "";
        for(int j=i; j<startPath.size(); j++) path.append("U");
        for(int j=i; j<destPath.size(); j++) path.push_back(destPath[j]);
        return path;
    }

    string getPath(TreeNode* root, int target, string &path) {
        if(root == nullptr) return "";
        if(root->val == target) return path;

        path.append("L");
        string lpath = getPath(root->left, target, path);
        path.pop_back();
        path.append("R");
        string rpath = getPath(root->right, target, path);
        path.pop_back();

        if(lpath != "") return lpath;
        if(rpath != "") return rpath;

        return "";
    }
};